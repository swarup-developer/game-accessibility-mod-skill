"""Validate the package, refresh its inventory, or build reproducible release ZIPs."""
import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT/'skills/accessibility-mod-development'
INVENTORY = SKILL/'references/inventory.json'
IGNORED = {'.git', '__pycache__', '.test-output', 'dist'}


def source_files(root):
    return sorted(p for p in root.rglob('*') if p.is_file() and not any(x in IGNORED for x in p.relative_to(root).parts))


def refresh():
    files = [{'path': p.relative_to(SKILL).as_posix(), 'bytes': p.stat().st_size,
              'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
             for p in source_files(SKILL) if p != INVENTORY]
    INVENTORY.write_text(json.dumps({'created_date': '2026-11-17', 'files': files}, indent=2)+'\n', encoding='utf-8')
    return len(files)


def validate():
    text = (SKILL/'SKILL.md').read_text(encoding='utf-8')
    assert text.startswith('---\n'), 'SKILL.md must start with frontmatter'
    header = text.split('---', 2)[1]
    name = re.search(r'^name:\s*(.+)$', header, re.M)
    description = re.search(r'^description:\s*(.+)$', header, re.M)
    assert name and name.group(1) == SKILL.name and re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name.group(1)), 'Invalid skill name'
    assert description and 0 < len(description.group(1)) <= 1024, 'Invalid description'
    inventory = json.loads(INVENTORY.read_text(encoding='utf-8'))
    expected = {item['path'] for item in inventory['files']}
    assert len(expected) == len(inventory['files']), 'Duplicate inventory paths'
    actual = {p.relative_to(SKILL).as_posix() for p in source_files(SKILL) if p != INVENTORY}
    assert expected == actual, f'Inventory mismatch: {expected ^ actual}'
    for item in inventory['files']:
        path = (SKILL/item['path']).resolve()
        assert SKILL.resolve() in path.parents, 'Inventory path escapes the skill'
        assert hashlib.sha256(path.read_bytes()).hexdigest() == item['sha256'], f'Changed file: {item["path"]}'
    manifest = json.loads((SKILL/'references/source-manifest.json').read_text(encoding='utf-8'))
    for item in manifest['github_files']:
        data = (SKILL/item['bundled_path']).read_bytes()
        assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest() == item['source_blob_sha'], item['bundled_path']
    curated = [SKILL/'SKILL.md']+list((SKILL/'references').glob('*.md'))+[ROOT/'README.md']+list((ROOT/'docs').glob('*.md'))
    links = 0
    for doc in curated:
        for link in re.findall(r'\]\(([^)]+)\)', doc.read_text(encoding='utf-8')):
            if link.startswith(('https:', 'http:')):
                continue
            filename, _, anchor = link.partition('#')
            target = (doc.parent/filename).resolve() if filename else doc
            assert ROOT.resolve() in target.parents, f'Link escapes package: {doc}: {link}'
            assert target.exists(), f'Broken link: {doc}: {link}'
            if anchor and target.suffix == '.md':
                headings = re.findall(r'^#{1,6}\s+(.+?)\s*$', target.read_text(encoding='utf-8'), re.M)
                slugs = {re.sub(r'[^\w\- ]', '', h.lower()).replace(' ', '-') for h in headings}
                assert anchor in slugs, f'Missing heading: {doc}: {link}'
            links += 1
    config = json.loads((ROOT/'compatibility.json').read_text(encoding='utf-8'))
    assert set(config['agents']) == {'Codex', 'Claude', 'Gemini', 'Antigravity', 'Freebuff'}
    for p in source_files(SKILL):
        assert not p.is_symlink() and p.suffix.lower() not in {'.dll', '.exe', '.pdb', '.pyc'}, f'Unexpected binary or link: {p}'
    return {'skill_files': len(actual)+1, 'curated_links': links, 'original_blob_hashes': len(manifest['github_files'])}


def write_zip(path, files, prefix):
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for file, relative in files:
            info = zipfile.ZipInfo(prefix+'/'+relative, date_time=(2026, 11, 17, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, file.read_bytes(), compresslevel=9)


def build():
    validate()
    version = (ROOT/'VERSION').read_text().strip()
    assert re.fullmatch(r'\d+\.\d+\.\d+', version), 'Version must be numeric SemVer'
    dist = ROOT/'dist'
    dist.mkdir(exist_ok=True)
    allowed = {'README.md', 'LICENSE', 'THIRD_PARTY_NOTICES.md', 'VERSION', 'compatibility.json', 'install.bat', 'uninstall.bat', 'install.ps1', 'RELEASE_NOTES.md', '.gitattributes', '.gitignore'}
    full = [(p, p.relative_to(ROOT).as_posix()) for p in source_files(ROOT)
            if p.relative_to(ROOT).parts[0] in {'skills', 'docs', 'scripts', '.github'} or p.relative_to(ROOT).as_posix() in allowed]
    skill = [(p, p.relative_to(SKILL).as_posix()) for p in source_files(SKILL)]
    full_path = dist/f'game-accessibility-mod-skill-{version}.zip'
    skill_path = dist/f'accessibility-mod-development-{version}.skill.zip'
    write_zip(full_path, full, f'game-accessibility-mod-skill-{version}')
    write_zip(skill_path, skill, SKILL.name)
    sums = ''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in [full_path, skill_path])
    (dist/'SHA256SUMS.txt').write_text(sums, encoding='utf-8')
    return {'archives': [str(full_path), str(skill_path)], 'checksums': str(dist/'SHA256SUMS.txt')}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['refresh', 'validate', 'build'])
    args = parser.parse_args()
    try:
        result = {'inventory_files': refresh()} if args.action == 'refresh' else validate() if args.action == 'validate' else build()
        print(json.dumps(result, indent=2))
        return 0
    except (AssertionError, OSError, ValueError) as exc:
        print('Package check failed: '+str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
