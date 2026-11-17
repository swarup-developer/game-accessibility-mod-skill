"""Review a declared binding inventory; never assign keys or certify live controls."""
import argparse
import json
import sys
from pathlib import Path

MODIFIERS = {'CTRL': 'CTRL', 'CONTROL': 'CTRL', 'ALT': 'ALT', 'SHIFT': 'SHIFT', 'WIN': 'WIN', 'WINDOWS': 'WIN'}


def normalize(key):
    parts = [p.strip().upper().replace(' ', '') for p in key.split('+')]
    parts = [MODIFIERS.get(p, p) for p in parts]
    return '+'.join(sorted(parts))


def audit(document):
    findings, seen, functions = [], [], set()
    if not isinstance(document, dict):
        raise ValueError('Inventory must be a JSON object.')
    bindings = document.get('bindings')
    if not isinstance(bindings, list):
        raise ValueError('Inventory must contain a bindings list.')
    for entry in bindings:
        if not isinstance(entry, dict) or not entry.get('action'):
            raise ValueError('Each binding needs an action name.')
        action, key = entry['action'], entry.get('key')
        contexts = entry.get('contexts')
        if not isinstance(contexts, list) or not contexts or not all(isinstance(x, str) and x for x in contexts):
            raise ValueError(f'{action}: supply explicit non-empty contexts.')
        if not key:
            findings.append({'action': action, 'reason': 'unbound', 'detail': 'No key assigned; no safe key is inferred.'})
            continue
        if not isinstance(key, str):
            raise ValueError(f'{action}: key must be text or null.')
        canonical = normalize(key)
        parts = canonical.split('+')
        if '' in parts:
            raise ValueError(f'{action}: malformed key combination.')
        if any(p in MODIFIERS.values() for p in parts) and not entry.get('user_requested', False):
            findings.append({'action': action, 'reason': 'unrequested_chord', 'detail': 'Prefer a verified single key; do not invent modifier shortcuts.'})
        if canonical in {normalize(x) for x in ['Alt+Space', 'Alt+F4', 'Ctrl+Alt+Delete']}:
            findings.append({'action': action, 'reason': 'system_shortcut', 'detail': 'This combination has a Windows system function; review the conflict.'})
        if any(p in {'INSERT', 'CAPSLOCK', 'NUMPAD0'} for p in parts):
            findings.append({'action': action, 'reason': 'reader_key_review', 'detail': 'Check actual screen-reader modifier/review settings.'})
        if entry.get('status') == 'verified' and not entry.get('evidence'):
            findings.append({'action': action, 'reason': 'missing_evidence', 'detail': 'A verified label needs a source/runtime evidence reference.'})
        if entry.get('status') != 'verified':
            findings.append({'action': action, 'reason': 'not_verified', 'detail': 'Declared inventory is not proof this input works in the installed game.'})
        for old in seen:
            overlap = '*' in contexts or '*' in old['contexts'] or bool(set(contexts) & set(old['contexts']))
            if canonical == old['key'] and overlap:
                findings.append({'action': action, 'reason': 'overlapping_binding', 'other_action': old['action']})
        seen.append({'action': action, 'key': canonical, 'contexts': contexts})
        if canonical in {f'F{i}' for i in range(1, 13)}:
            functions.add(canonical)
    if len(functions) == 12 and not document.get('full_function_row_requested', False):
        findings.append({'reason': 'function_row_sprawl', 'detail': 'The entire F1-F12 row was allocated without a recorded request.'})
    return {'status': 'needs_review' if findings else 'no_declared_conflicts', 'findings': findings,
            'note': 'This checks the supplied inventory only. Evidence strings are not independently verified; actual game/OS/reader conflicts and runtime behavior still need testing.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('inventory', type=Path)
    args = parser.parse_args()
    try:
        result = audit(json.loads(args.inventory.read_text(encoding='utf-8-sig')))
        print(json.dumps(result, indent=2))
        return 1 if result['findings'] else 0
    except (OSError, ValueError, KeyError) as exc:
        print(json.dumps({'error': str(exc)}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
