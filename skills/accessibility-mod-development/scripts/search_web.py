"""Create web research links; no scraping or invented search results."""
import argparse
import json
import sys
import urllib.parse
import webbrowser


def links(query, mode='primary'):
    suffixes = {'primary': ['official documentation', 'site:github.com'],
                'blogs': ['engineering blog', 'accessibility mod postmortem'],
                'compatibility': ['mod loader compatibility version', 'site:github.com issues'],
                'all': ['', 'official documentation', 'engineering blog', 'site:github.com']}[mode]
    return [{'query': (query+' '+suffix).strip(),
             'url': 'https://www.google.com/search?' + urllib.parse.urlencode({'q': (query+' '+suffix).strip()})} for suffix in suffixes]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--query', required=True)
    parser.add_argument('--mode', choices=['primary', 'blogs', 'compatibility', 'all'], default='primary')
    parser.add_argument('--open', action='store_true', help='Explicitly open generated search URLs in your browser.')
    args = parser.parse_args()
    if not args.query.strip():
        parser.error('A non-empty query is required.')
    result = links(args.query, args.mode)
    if args.open:
        for item in result:
            webbrowser.open(item['url'])
    print(json.dumps({'search_links': result, 'results_fetched': False,
                      'note': 'These are query links, not findings. Do not include private source, logs, or secrets in public searches.'}, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
