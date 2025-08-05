# 📌 GitHub Sync Walkthrough (Ubuntu)

## 1️⃣ Install Git
\`\`\`bash
sudo apt update
sudo apt install git -y
git --version
\`\`\`

---

## 2️⃣ Configure Git (One time only)
\`\`\`bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
\`\`\`

---

## 3️⃣ Create Local Project Folder
\`\`\`bash
mkdir -p ~/git-folder/Nornir-Automation-Study
cd ~/git-folder/Nornir-Automation-Study
\`\`\`

---

## 4️⃣ Initialize Git
\`\`\`bash
git init
\`\`\`

---

## 5️⃣ Create a .gitignore File (Recommended)
\`\`\`plaintext
venv/
__pycache__/
*.log
\`\`\`

---

## 6️⃣ Add Files
\`\`\`bash
touch main.py
\`\`\`

---

## 7️⃣ Create GitHub Repository (Online)

1. Go to [GitHub New Repository](https://github.com/new)
2. Create a **new repo** (no README if files already exist locally).

---

## 8️⃣ Connect Local Repo to GitHub
\`\`\`bash
git remote add origin https://github.com/USERNAME/REPO_NAME.git
git remote -v
\`\`\`

---

### 9
 First Commit & Push
\`\`\`bash
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
\`\`\`

---

# 🔄 Daily Usage

## Create git-sync Script (Automation)
\`\`\`bash
sudo nano /usr/local/bin/git-sync
\`\`\`
Paste:
\`\`\`bash
#!/bin/bash
branch=$(git rev-parse --abbrev-ref HEAD)
git add .
git commit -m "${1:-Auto-sync commit}"
git push origin "$branch"
\`\`\`
Make it executable:
\`\`\`bash
sudo chmod +x /usr/local/bin/git-sync
\`\`\`

---

## Push Changes
\`\`\`bash
git-sync "Updated files"
\`\`\`

---

## Pull Updates
\`\`\`bash
git pull
\`\`\`

---

## Check Status
\`\`\`bash
git status
\`\`\`

---

# ⚡ Git Commands Quick Reference

| Command                          | Description                               |
|----------------------------------|-------------------------------------------|
| \`git init\`                     | Initialize a new repository              |
| \`git clone <url>\`              | Clone a repository from GitHub           |
| \`git add .\`                    | Stage all changes                        |
| \`git commit -m "message"\`      | Commit staged changes                    |
| \`git push origin main\`         | Push changes to GitHub                   |
| \`git pull origin main\`         | Pull updates from GitHub                 |
| \`git branch\`                   | List branches                            |
| \`git checkout -b new-branch\`   | Create and switch to a new branch        |
| \`git switch branch-name\`       | Switch branches                          |
| \`git merge branch-name\`        | Merge a branch into the current one      |
| \`git status\`                   | Show file change status                  |
| \`git log --oneline\`            | Show commit history                      |
| \`git diff\`                     | Show unstaged changes                    |
| \`git restore <file>\`           | Undo changes in a file                   |
| \`git reset --hard HEAD~1\`      | Undo last commit                         |
| \`git branch -d branch-name\`    | Delete a branch                          |
| \`git stash / git stash pop\`    | Temporarily store and restore changes    |
