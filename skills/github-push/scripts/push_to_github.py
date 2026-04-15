#!/usr/bin/env python3
"""Push file content to a GitHub repository via the Contents API."""
import argparse
import base64
import json
import urllib.request
import urllib.error
import sys


def push_file(token, repo, path, content, branch="main", message=None):
    if message is None:
        message = f"Update {path}"

    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "github-push-skill",
    }

    # Check if file exists to get its SHA
    sha = None
    try:
        req = urllib.request.Request(url + f"?ref={branch}", headers=headers, method="GET")
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            sha = data.get("sha")
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise

    encoded = base64.b64encode(content.encode("utf-8")).decode("utf-8")
    payload = {
        "message": message,
        "content": encoded,
        "branch": branch,
    }
    if sha:
        payload["sha"] = sha

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={**headers, "Content-Type": "application/json"},
        method="PUT",
    )

    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read().decode())
        return result


def main():
    parser = argparse.ArgumentParser(description="Push a file to GitHub")
    parser.add_argument("--token", required=True, help="GitHub personal access token")
    parser.add_argument("--repo", required=True, help="Repository in owner/repo format")
    parser.add_argument("--path", required=True, help="File path inside the repository")
    parser.add_argument("--content", required=True, help="File content (string)")
    parser.add_argument("--branch", default="main", help="Target branch")
    parser.add_argument("--message", default=None, help="Commit message")
    args = parser.parse_args()

    try:
        result = push_file(args.token, args.repo, args.path, args.content, args.branch, args.message)
        print(json.dumps(result, indent=2))
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.read().decode()}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
