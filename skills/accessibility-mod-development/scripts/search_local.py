"""Search local source text with bounded output; never change files or upload text."""
import argparse
import fnmatch
import json
import os
import sys
from pathlib import Path

SKIP = {'.git', 'node_modules', 'bin', 'obj', '__pycache__', '.venv', 'venv'}
EXTENSIONS = {'.cs', '.lua', '.py', '.cpp', '.c', '.h', '.hpp', '.md', '.txt', '.json', '.yaml', '.yml', '.gd', '.rpy', '.ps1', '.toml', '.ini', '.cfg', '.xml', '.java', '.ts', '.js', '.rst', '.inputactions', '.template', '.idl', '.resx'}


def search(root, query, globs=(), limit=100, max_bytes=2_000_000, context=1):
    matches, skipped = [], 0
    for folder, directories, filenames in os.walk(root, followlinks=False):
        directories[:] = sorted(d for d in directories if d not in SKIP and not (Path(folder)/d).is_symlink())
        for filename in sorted(filenames):
            path = Path(folder)/filename
            if path.is_symlink() or path.suffix.lower() not in EXTENSIONS:
                continue
            relative = path.relative_to(root).as_posix()
            if globs and not any(fnmatch.fnmatch(relative, pattern) or fnmatch.fnmatch(filename, pattern) for pattern in globs):
                continue
            try:
                if path.stat().st_size > max_bytes:
                    skipped += 1
                    continue
                lines = path.read_text(encoding='utf-8-sig').splitlines()
            except (OSError, UnicodeError):
                skipped += 1
                continue
            for index, line in enumerate(lines):
                if query.casefold() in line.casefold():
                    clipped = lines[max(0, index-context):index+context+1]
                    matches.append({'path': relative, 'line': index+1, 'text': line[:2000],
                                    'context_start': max(1, index+1-context),
                                    'context': [text[:2000] for text in clipped],
                                    'text_truncated': any(len(text) > 2000 for text in clipped)})
                    if len(matches) >= limit:
                        return {'matches': matches, 'limit_reached': True, 'skipped_files': skipped}
    return {'matches': matches, 'limit_reached': False, 'skipped_files': skipped}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--query', required=True, help='Literal, case-insensitive text; not a regular expression.')
    parser.add_argument('--glob', action='append', default=[])
    parser.add_argument('--limit', type=int, default=100)
    parser.add_argument('--context', type=int, default=1)
    args = parser.parse_args()
    if not args.query.strip() or not 1 <= args.limit <= 1000 or not 0 <= args.context <= 10:
        parser.error('Use a non-empty query, limit 1 to 1000, and context 0 to 10.')
    if not args.root.is_dir():
        parser.error('The source folder does not exist.')
    result = search(args.root.resolve(), args.query, args.glob, args.limit, context=args.context)
    result['note'] = 'Text matches are discovery evidence, not proof that a game action runs.'
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
