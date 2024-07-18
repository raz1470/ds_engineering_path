Contents
==
- [Contents](#contents)
- [What is Git?](#what-is-git)
- [Installing Git](#installing-git)
- [Basic Git commands](#basic-git-commands)
- [Ignoring files](#ignoring-files)
- [Cloning this repo](#cloning-this-repo)

<!--intro-start-->
# What is Git?
Git is a version control system that allows multiple people to collaborate on a project.

Some key concepts to understand are:

- **Repository (Repo)** - A Git repository is like a project folder that contains all the files and the entire history of changes for that project. It can be local (on your computer) or remote (on a server, like GitHub or GitLab).
- **Commit** - A commit is a snapshot of the changes made to the files in your repository at a specific point in time. Commits are accompanied by a commit message that describes the changes made.
- **Branch** - Git allows you to create branches, which are essentially separate lines of development. This is useful for working on new features or bug fixes without affecting the main (often called "master") branch until you're ready.
- **Merge** - Merging is the process of combining changes from one branch into another. After completing work in a feature branch, for example, you might merge those changes back into the main branch.
- **Pull and push** - Pulling refers to fetching changes from a remote repository to your local repository. Pushing is the act of sending your local changes to the remote repository. These actions are crucial for collaboration with others.
- **Remote** - A remote is a repository that is hosted on a server (e.g., GitHub, GitLab). You can push your changes to a remote repository to share your work with others and pull changes made by others into your local repository.
- **Clone** - Cloning is the process of creating a copy of a remote repository on your local machine. It's the initial step when you want to start working on a project that already exists on a remote server.
- **Pull request (PR)** - In the context of platforms like GitHub or GitLab, a pull request is a way to propose changes to a repository. It allows others to review your changes before merging them into the main branch.
- **Conflict** - Conflicts occur when Git can't automatically reconcile changes from different branches. Resolving conflicts involves manually merging conflicting changes.

# Installing Git
You can install git [here](https://git-scm.com/downloads)

# Basic Git commands
The following commands are used in a typical workflow:

| Command | What does it do | 
| ---- | -------------- |
| `git remote add <remote_name> <remote_url>` | Adds a new remote repository |
| `git clone <repository_url>` | Creates a copy of a remote repository on your local machine |
| `git branch` | Lists all local branches, with the current branch highlighted |
| `git checkout <branch_name>` | Switches to the specified branch |
| `git branch <new-branch>` | Create new branch |
| `git add .` | Adds all changes in the working directory to the staging area |
| `git commit -m "Commit message"` | Commits the staged changes with a descriptive commit message |
| `git fetch` | Fetches changes from a remote repository without merging them into the current branch |
| `git pull` | Fetches changes from a remote repository and merges them into the current branch. |
| `git push` | Pushes local commits to the remote repository |
| `git status` | Shows the status of changes as untracked, modified, or staged |

# Ignoring files
A `gitignore` file specifies intentionally untracked files that Git should ignore.

Checkpoint files created by Jupyter Notebook, all the files created from your virtual environment etc.

You can see any example of a `gitignore` file in the root directory.

# Cloning this repo
Go to the terminal in VSC, navigate to where you want to clone this repo and run the following: `git clone <git@vie.git.bwinparty.com:marketing-data-science/a_data_scientists_guide_to_software_engineering.git>`