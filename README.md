# test-basic-git-commands
This repository was created to test basic git commands

# Basic Git commands and their application
[Git docs](https://git-scm.com/docs)

## Setup & Configuration
- `git config --global user.name "Seu Nome"`: Sets the name associated with your commits.
- `git config --global user.email "[email]"`: Sets the email address associated with your commits.
- `git config --list`: Displays all current configuration settings.

## Initializing & Creating Projects
- `git init`: Initializes a new, empty Git repository in the current directory.
- `git clone [url]`: Downloads an existing repository and its entire version history to your local machine.

## The Basic Workflow (Snapshotting)
- `git status`: Lists which files are modified, staged, or untracked.
- `git add [file]`: Stages a specific file for the next commit. Use git add . to stage all changes in the current directory.
- `git commit -m "[message]"`: Records the staged snapshot permanently in the version history with a descriptive message.
- `git log`: Displays the commit history for the current branch.

## Branching & Merging
- `git branch`: Lists all local branches; the asterisk indicates the current branch.
- `git checkout [branch-name]`: Switches from the current branch to the specified one.
- `git checkout -b [branch-name]`: Creates a new branch and immediately switches to it.
- `git merge [branch]`: Combines the history of the specified branch into the current branch.

## Sharing & Synchronizing
- `git push [remote] [branch]`: Uploads local branch commits to the remote repository.
- `git pull`: Fetches changes from the remote and merges them into your current local branch.
- `git remote add [name] [url]`: Connects your local repository to a remote server.

