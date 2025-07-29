
# Backend Dev & Deployment Cheatsheet

## 1. Local Environment Variables (FastAPI with Pydantic Settings)

### Windows (PowerShell)
```powershell
$env:ENV_FILE=".env.testing"
# Or for a single variable:
$env:MY_SETTING="some_value"
```

### Linux/macOS (Bash/Zsh)
```bash
export ENV_FILE=".env.testing"
# Or for a single variable:
export MY_SETTING="some_value"
```

---

## 2. Running Tests

```bash
python -m pytest
```

---

## 3. Git Tagging for Deployments (Annotated Tags for Releases)

### Create a Tag (on current branch's latest commit)
```bash
# Ensure local branch is up-to-date first
git checkout main
git pull origin main
git tag -a v0.0.1 -m "My release message"
```

### Verify Local Tags
```bash
git tag         # List all local tags
git show v0.0.1 # Show tag details
```

### Push Tags to GitHub
```bash
git push origin v0.0.1      # Push a specific tag
git push origin --tags      # Push all local tags
```

### Delete Tags

#### Delete Local Tag
```bash
git tag -d v1.0.0
```

#### Delete Remote Tag (on GitHub)
```bash
git push origin :v1.0.0      # (Note the colon)
# OR
git push --delete origin v1.0.0
```
