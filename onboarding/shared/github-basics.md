Table of Contents
---
- [Quick Start: To Branch or to Fork? That is the question](#quick-start-to-branch-or-to-fork-that-is-the-question)
  - [1. Minimal Customization Needed](#1-minimal-customization-needed)
    - [Main Branch or “Template” Folder](#main-branch-or-template-folder)
  - [2. Each Member Customizes and Shares Changes](#2-each-member-customizes-and-shares-changes)
    - [Option A: Branches in One Repo](#option-a-branches-in-one-repo)
    - [Option B: Forks](#option-b-forks)
  - [3. Template-Only Repository](#3-template-only-repository)
  - [Typical Recommendation](#typical-recommendation)
  - [Key Concepts](#key-concepts)


# Quick Start: To Branch or to Fork? That is the question


This guide provides essential steps for working on a GitHub repository, whether you’re a lab member, a direct collaborator or working on your own fork. 

## 1. Minimal Customization Needed

### Main Branch or “Template” Folder
- **Description**: Place the template script in the main branch (or a dedicated “template” folder) in the primary repository.
- **How to Use**: Each user clones the repo and copies the script as needed.
- **Pros**:
  - Very straightforward; no branching or forking required.
  - Everyone has immediate access to the most up-to-date template.
- **Cons**:
  - Personal modifications can accidentally get committed to main if not careful.

---

## 2. Each Member Customizes and Shares Changes

### Option A: Branches in One Repo
1. **Main** branch holds the official template.
2. Each user creates a **new branch** (e.g., `username-template`) for their customization.
3. If improvements are made, open a **Pull Request** to merge them back to the official template.

**Pros**:
- Simple to see and merge each person’s changes within one repo.  
- Good if all members have collaborator access and are comfortable with Git branching.

**Cons**:
- Multiple branches can become cluttered if many users are customizing the template differently.

### Option B: Forks
1. The main repo hosts the “official” template.
2. Each user **forks** that repo to their own GitHub account.
3. They clone their fork and customize the template locally.
4. If they have useful updates, they open a Pull Request from their fork to the main repo.

**Pros**:
- Ideal for users without direct collaborator rights.
- Keeps each person’s work isolated in their own fork.

**Cons**:
- Users must pull changes from the main repo to keep their forks synced.
- Slightly more setup to manage “upstream” vs. “origin” remotes.

---

## 3. Template-Only Repository

- **Dedicated “Template” Repo**: Store the script in a separate repo that serves solely as a template source.
- Users clone or fork this template repo for any new project.

**Pros**:
- Clearly separates the template from active project code.
- Reduces confusion about which scripts are “template” vs. “in development.”

**Cons**:
- Another repository to maintain.
- Must manually pull updates if the template itself evolves over time.

---

## Typical Recommendation

- **If frequent collaboration or shared improvements are expected**:
  - **Branches** (same repo) are straightforward for active team members.
  - **Forks** are best if some members only need read access or if the project is open to external contributors.
- **If the template changes rarely** or each member largely works independently:
  - Keeping the script on the **main** branch (or in a dedicated folder) can be enough.

Choose the method that best fits your lab’s workflow, collaboration style, and coding comfort level.  
```
## Key Concepts
- **Fork**: Your personal copy of another person’s repository (good if you’re *not* a collaborator).  
- **Clone**: Make a local copy of a repo on your computer.  
- **Commit**: A snapshot of changes. Commit frequently with clear messages.  
- **Push**: Send your local commits to GitHub.  
- **Pull**: Update your local copy with remote changes.  
- **Branch**: An isolated line of development. Use branches for new features or fixes.  
- **Pull Request (PR)**: Propose merging your branch/fork changes into the main repo.
- **Merge**: Combine changes from one branch into another.
- **Upstream**: The original repository you forked from.
- **Origin**: Your personal copy of the repository (your fork).
- **Remote**: A version of your repository hosted on GitHub.
- **Main Branch**: The default branch in a repository (often called `main` or `master`).
