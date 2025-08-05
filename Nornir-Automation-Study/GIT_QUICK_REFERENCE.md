# ⚡ Git Commands Quick Reference

This document provides a quick list of commonly used Git commands.

---

## 🔹 Git Setup
\`\`\`bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
\`\`\`

---

## 🔹 Create Repo
\`\`\`bash
git init
git clone <url>
\`\`\`

---

## 🔹 Stage & Commit
\`\`\`bash
git add .
git commit -m "message"
\`\`\`

---

## 🔹 Remote Connection
\`\`\`bash
git remote add origin <url>
git remote -v
\`\`\`

---

## 🔹 Push & Pull
\`\`\`bash
git push origin main
git pull origin main
\`\`\`

---

## 🔹 Branches
\`\`\`bash
git branch
git checkout -b new-branch
git switch branch-name
git merge branch-name
\`\`\`

---

## 🔹 Status & Logs
\`\`\`bash
git status
git log --oneline
git diff
\`\`\`

---

## 🔹 Undo Changes
\`\`\`bash
git restore <file>
git reset --hard HEAD~1
\`\`\`

---

## 🔹 Delete Branch
\`\`\`bash
git branch -d branch-name
\`\`\`

---

## 🔹 Stash Changes
\`\`\`bash
git stash
git stash pop
\`\`\`

---
