"""Check verification-record attachments and hashes; this does not prove gameplay."""
import argparse
import hashlib
import json
import sys
from pathlib import Path

STAGES = ('implemented', 'built', 'installed', 'runtime_observed', 'screen_reader_confirmed')


def check(record, base, required=()):
    problems, checked = [], 0
    if not isinstance(record, dict):
        raise ValueError('Verification record must be a JSON object.')
    stages = record.get('stages')
    if not record.get('feature') or not isinstance(stages, dict):
        raise ValueError('Record needs a feature and stages object.')
    for stage, item in stages.items():
        if stage not in STAGES or not isinstance(item, dict) or item.get('status') not in {'pending', 'passed', 'failed'}:
            raise ValueError('Unknown stage or status: '+stage)
        if item['status'] != 'passed':
            continue
        evidence = item.get('evidence')
        if not isinstance(evidence, list) or not evidence:
            problems.append(f'{stage}: passed without evidence attachments')
            continue
        for attachment in evidence:
            if not isinstance(attachment, dict) or not attachment.get('path') or not attachment.get('description'):
                problems.append(f'{stage}: attachment needs path and description')
                continue
            path = Path(attachment['path'])
            if not path.is_absolute():
                path = base/path
            if not path.is_file():
                problems.append(f'{stage}: evidence file missing: {attachment["path"]}')
                continue
            expected = attachment.get('sha256', '')
            digest = hashlib.sha256()
            with path.open('rb') as stream:
                for chunk in iter(lambda: stream.read(65536), b''):
                    digest.update(chunk)
            if len(expected) != 64 or digest.hexdigest() != expected.lower():
                problems.append(f'{stage}: evidence hash absent or changed: {attachment["path"]}')
                continue
            checked += 1
    for stage in required:
        if stages.get(stage, {}).get('status') != 'passed':
            problems.append(stage+': required stage has not passed')
    return {'feature': record['feature'], 'attachment_checks_passed': not problems,
            'checked_attachments': checked, 'problems': problems,
            'note': 'A matching evidence file does not establish that its claims are true. Runtime actions and audible screen-reader behavior require independent observation.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('record', type=Path)
    parser.add_argument('--require', choices=STAGES, action='append', default=[])
    args = parser.parse_args()
    try:
        result = check(json.loads(args.record.read_text(encoding='utf-8-sig')), args.record.resolve().parent, args.require)
        print(json.dumps(result, indent=2))
        return 0 if result['attachment_checks_passed'] else 1
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({'error': str(exc)}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
