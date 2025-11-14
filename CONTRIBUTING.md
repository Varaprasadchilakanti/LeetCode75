
## Welcome
Thank you for contributing to **LeetCode75**. This project follows a disciplined, team‑grade workflow designed for clarity, reproducibility, and long‑term resilience. Please read and follow these guidelines before submitting changes.

---

## Workflow Overview

### Clone the repository
```bash
git clone git@github.com:Varaprasadchilakanti/LeetCode75.git
cd LeetCode75
```

### Create a feature branch
```bash
git checkout -b feature/<short-description>
```
Example: `feature/stack-module`

### Synchronize with remote before committing
```bash
git fetch origin
git pull --rebase origin main
```

### Stage changes selectively
```bash
git add stack/
git diff --cached
```

### Commit with professional messaging
```bash
git commit -m "Add stack module with initial problem stubs and structured layout"
```

### Push branch
```bash
git push origin feature/stack-module
```

### Open a Pull Request
- Ensure CI checks pass (lint/tests).  
- Request review from teammates.  

### Merge to main
- After approval, rebase and merge.  
- Locally update:
```bash
git checkout main
git pull --rebase origin main
```

---

## Commit Message Convention

- **Prefixes:** Add, Refactor, Fix, Docs, Test, Chore  
- **Subject line:** ≤ 72 characters, imperative mood  
- **Optional body:** rationale, context, decisions  

Examples:
- `Add LC2390_Removing_Stars_From_String.py with stack-based solution`  
- `Refactor hashmap_set layout for clarity and SOLID alignment`  
- `Docs: update README with stack module overview`  

Reference: [Conventional Commits](https://www.conventionalcommits.org/)

---

## Coding Standards

- **File naming:** `LC<problem_number>_<slug>.py`  
- **Style:** PEP8, type hints, docstrings  
- **Architecture:** SOLID principles, clean separation of concerns  
- **Tests:** Use `pytest` for validation  

---

## Collaboration Practices

- **Branch protection:** `main` is protected; all changes via Pull Request  
- **CI/CD:** GitHub Actions run lint (`flake8`, `mypy`) and tests (`pytest`)  
- **Documentation:** Update README when structure or intent changes  
- **Hygiene:** `.gitignore` excludes editor/system artifacts  

---

## Troubleshooting

**SSH agent not running:**
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

**Permission denied (publickey):**
- Verify key added to GitHub  
- Test with:
```bash
ssh -T git@github.com
```

**Merge conflicts:**
```bash
git status
# resolve conflicts
git add <resolved-files>
git rebase --continue
```

---

## References

- [Git Book](https://git-scm.com/book/en/v2)  
- [GitHub SSH setup](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)  
- [Conventional Commits](https://www.conventionalcommits.org/)  
- [GitHub Branch Protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches)
