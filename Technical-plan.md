How to Clone a GitHub Repository and Work on Your Own Branch in VS Code

1. Open Visual Studio Code
You don’t need to manually create a folder yet.

2. Copy the GitHub repository URL
Go to the repository page on GitHub

Click the green Code button

Copy the URL using HTTPS or SSH, e.g.:


https://github.com/PeterDong1997/EasyMeds-Flask.git

3. lone the repository in VS Code
Open the Command Palette:
Ctrl + Shift + P (Windows) or Cmd + Shift + P (Mac)

Type and select:

Git: Clone

Paste the repository URL

Choose a local folder to save the project
After cloning, click Open when prompted

4.  Create a new local branch
After the repository is opened in VS Code:

Open the Source Control panel (branch icon on the left)
On the bottom left of VS Code (status bar), click the current branch name (e.g., main)
Select Create new branch…

Name your branch, e.g.:

css
Copy
Edit
peter-edit-header
VS Code will automatically switch to your new branch

You are now editing on your own branch — changes here won’t affect main until you create a pull request.

5. Edit, commit, and push your branch
Make your changes in VS Code

Go to Source Control

Write a commit message and click the ✓ (check mark) icon

Then click the … menu > Push

* The first time you push a new branch, Git will ask if you want to publish it — select Yes or Publish branch.

6. (Optional) Open a Pull Request on GitHub
Go to the repository page on GitHub

You will see a prompt:

“Compare & pull request” for your new branch

Click it to open a pull request and propose your changes to be merged into main