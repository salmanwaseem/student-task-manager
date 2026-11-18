# Lab Assignment 4 — Git and GitHub Report

**Course:** CSC418 DevOps for Cloud Computing  
**Project:** Student Task Manager  
**Repository:** https://github.com/salmanwaseem/student-task-manager

## 1. Git vs GitHub; add, commit, push
Git is the version-control program that records changes locally. GitHub hosts Git repositories online and provides collaboration tools. `git add` stages selected file changes, `git commit` saves a snapshot in the local history, and `git push` sends commits to a remote branch.

## 2. Branches, pull requests, and merge conflicts
Branches isolate feature work without breaking the shared `main` branch. Pull requests let contributors inspect diffs, discuss changes, and merge them. A merge conflict occurs when Git cannot automatically reconcile incompatible edits, such as two branches replacing the same README status line.

## 3. Fetch vs pull; merge vs rebase
`git fetch` downloads remote changes without updating the current working branch. `git pull` fetches and then integrates them, usually by merge or rebase. Merge joins histories, potentially producing a merge commit. Rebase reapplies commits onto a new base, rewriting their commit IDs; it should be used carefully on shared branches.

## 4. GitHub Issues and Actions
Issues track the validation, completion, deletion, documentation, and conflict tasks with labels. GitHub Actions automatically executes the unittest suite for pushes and pull requests; the recorded failed and successful runs demonstrate the red-green workflow.

## 5. Difficulty and resolution
The deliberate README conflict in PR #10 was the main integration challenge. Two branches started at `Project status: Planning`, then set that same line to different values. PR #9 merged the Testing version first. GitHub rejected an attempted merge of PR #10 with a conflict. A two-parent resolution commit kept the final `Project status: Ready for release` line while preserving unrelated README content, after which PR #10 merged.

## Workflow evidence and reflection
- **Feature PRs:** #6, #7, #8 (all merged)
- **Conflict demonstration PRs:** #9 and #10 (both merged)
- **Initial failed Actions run:** https://github.com/salmanwaseem/student-task-manager/actions/runs/44263434800
- **First recorded successful Actions run:** https://github.com/salmanwaseem/student-task-manager/actions/runs/44263610867
- **Conflict PR:** https://github.com/salmanwaseem/student-task-manager/pull/10

The branch and commit history provides the actual evidence. Capture browser screenshots of the repository, Issues, merged PRs, conflicting PR, test runs, and release as required by the submission instructions.

**Student reflection note:** Review and personalize this report so the viva answers reflect your own understanding and the work you can demonstrate.
