---
name: github-push
description: Push any file or content to a GitHub repository. Use when the user asks to upload, save, commit, or push files/code/content to GitHub, or when working with a remote GitHub repo that needs updates.
---

# GitHub Push Skill

Push files or content to a GitHub repository using either the GitHub API or local `git` commands.

## Quick Reference

| Approach | Best For | Requirements |
|----------|----------|--------------|
| **GitHub API** | One-off file uploads, no local git setup | GitHub token, repo write access |
| **Git CLI** | Multi-file changes, existing cloned repo | Git installed, repo cloned locally |

## GitHub API Approach (Recommended for Simple Pushes)

Use the bundled script for reliable single-file pushes without needing local git configuration.

```bash
python scripts/push_to_github.py \
  --token <GITHUB_TOKEN> \
  --repo <owner/repo> \
  --path <file-path-in-repo> \
  --content "file content here" \
  --branch main \
  --message "commit message"
```

### Example

```bash
python scripts/push_to_github.py \
  --token ghp_xxx \
  --repo myuser/myrepo \
  --path docs/guide.md \
  --content "# Hello World" \
  --branch main \
  --message "Add guide"
```

The script auto-detects whether the file exists and updates it (with SHA) or creates it.

## Git CLI Approach

When the repository is already cloned locally or multiple files need to be committed:

```bash
git add .
git commit -m "commit message"
git push origin <branch>
```

If the repo is not yet initialized or linked:

```bash
git init
git remote add origin https://github.com/<owner>/<repo>.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

## Getting a GitHub Token

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate a new token with at least the `repo` scope
3. Use it with the API script or HTTPS git authentication (`https://<token>@github.com/...`)

## Notes

- Always prefer the API script for quick single-file pushes to save time.
- For private repos, ensure the token has `repo` scope.
- The API script defaults to the `main` branch.
