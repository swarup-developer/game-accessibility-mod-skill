"""Search GitHub repositories, issues, or code through its read-only API."""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request


class SameHostRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, new_url):
        parsed = urllib.parse.urlparse(new_url)
        if parsed.scheme != 'https' or parsed.hostname != 'api.github.com':
            raise ValueError('Refusing an API redirect to another host.')
        return super().redirect_request(request, fp, code, msg, headers, new_url)


def search_url(kind, query, repo=None, limit=20):
    if repo:
        if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repo):
            raise ValueError('Repository must be owner/name, without a URL.')
        query = f'repo:{repo} {query}'
    return 'https://api.github.com/search/' + kind + '?' + urllib.parse.urlencode({'q': query, 'per_page': limit})


def search(kind, query, repo=None, limit=20):
    url = search_url(kind, query, repo, limit)
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'game-accessibility-mod-skill/0.1.0', 'X-GitHub-Api-Version': '2022-11-28'}
    token = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = 'Bearer ' + token
    opener = urllib.request.build_opener(SameHostRedirect())
    request = urllib.request.Request(url, headers=headers, method='GET')
    with opener.open(request, timeout=25) as response:
        payload = response.read(5_000_001)
        if len(payload) > 5_000_000:
            raise ValueError('Search response exceeded the size limit; narrow the query.')
        data = json.loads(payload)
    if not isinstance(data.get('items'), list):
        raise ValueError('GitHub did not return a search result list.')
    results = [{'name': item.get('full_name') or item.get('title') or item.get('path'),
                'url': item.get('html_url'), 'description': item.get('description'),
                'repository': (item.get('repository') or {}).get('full_name')} for item in data['items']]
    return {'kind': kind, 'total_count': data.get('total_count'),
            'incomplete_results': data.get('incomplete_results', False), 'results': results,
            'note': 'Search hits are leads. Inspect the matching version, source, and license before reuse.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--kind', choices=['repositories', 'issues', 'code'], default='repositories')
    parser.add_argument('--query', required=True)
    parser.add_argument('--repo', help='Optional owner/name scope.')
    parser.add_argument('--limit', type=int, default=20)
    args = parser.parse_args()
    if not args.query.strip() or not 1 <= args.limit <= 100:
        parser.error('Use a non-empty query and limit 1 to 100.')
    try:
        print(json.dumps(search(args.kind, args.query, args.repo, args.limit), ensure_ascii=True, indent=2))
        return 0
    except urllib.error.HTTPError as exc:
        messages = {401: 'Authentication is required or invalid. Code search normally needs an authenticated GitHub account.',
                    403: 'GitHub denied the request. Check permissions or the API rate limit.',
                    429: 'GitHub rate limit reached. Try later; no automatic retry was attempted.'}
        print(json.dumps({'error': messages.get(exc.code, 'GitHub search request failed.'), 'http_status': exc.code}), file=sys.stderr)
    except (OSError, ValueError) as exc:
        print(json.dumps({'error': str(exc)}), file=sys.stderr)
    return 2


if __name__ == '__main__':
    sys.exit(main())
