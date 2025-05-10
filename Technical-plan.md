#  How to Clone a GitHub Repository and Work on Your Own Branch in VS Code

This guide walks you through cloning the project, creating your own branch, and pushing your changes using Visual Studio Code.

---
## Video Tutorial

[How to Clone a GitHub Repository into VS Code | Step-by-Step Guide](https://www.youtube.com/watch?v=DdRCU1DUYE8)
---

## 1️ Open Visual Studio Code

You don’t need to manually create a folder in advance.

---

## 2️ Copy the GitHub Repository URL

- Go to the GitHub repository page:  
  [`https://github.com/PeterDong1997/EasyMeds-Flask.git`](https://github.com/PeterDong1997/EasyMeds-Flask.git)
- Click the green **Code** button  
- Copy the URL using **HTTPS** or **SSH**

---

## 3️ Clone the Repository in VS Code

- Open the Command Palette:  
  `Ctrl + Shift + P` (Windows) or `Cmd + Shift + P` (Mac)
- Type and select:

Git: Clone

- Paste the repository URL
- Choose a local folder to save the project
- Once cloning is complete, click **Open** when prompted

---

## 4️ Create a New Local Branch

Once inside the project folder:

- Open the **Source Control** panel (left sidebar, branch icon)
- At the bottom-left of VS Code, click the current branch name (e.g., `main`)
- Select **Create new branch…**
- Name your new branch, e.g.:
peter-edit-header

- VS Code will automatically switch to your new branch

✅ You are now working on your **own branch**. Your changes won’t affect `main` until you submit a pull request.

---

## 5️ Edit, Commit, and Push Your Branch

- Make your changes in VS Code
- Open the **Source Control** panel
- Enter a commit message (e.g., `Update homepage layout`)
- Click the ✓ (check mark) icon to commit
- Click the `…` menu > **Push**

💡 If this is the first time pushing this branch, click **Publish Branch** when prompted.

---

## 6️ (Optional) Create a Pull Request on GitHub

- Go to the GitHub repository page
- You’ll see a prompt:

> “Compare & pull request” for your new branch

- Click it to propose merging your branch into `main`
