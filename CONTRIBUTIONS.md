# Contributions

## GitHub Collaboration Instructions ##
Main Branch: This is the latest and most stable version of your project’s code base.
* Workflow Overview:
    * Each team member should create a personal branch based on the main branch.
    * Develop and test within your personal branch. Once your changes are final, submit your branch for code review so others can provide feedback.
    * Once approved, submit a pull request (PR). The PR process includes a review, and then the designated supervisor merges the approved changes into the main branch.
Steps for Creating Your Own Branch:
1. Clone the repository in your terminal.
2. Create a new branch: git checkout -b your_branch_name.
3. Push the branch to the repo: git push origin your_branch_name (your branch will initially mirror the main branch).
Making Changes in Your Branch:
1. Make edits as needed.
2. Stage the changes: git add .
3. Commit with a message: git commit -m "Describe your changes"
4. Push updates: git push origin your_branch_name
    * These changes remain isolated to your branch until merged into the main branch.
Submitting and Merging Changes:
1. Once the team is ready to review, go to the repository's Pull Requests tab.
2. Click New Pull Request.
3. Confirm you’re comparing your branch to the main branch.
4. Click Create Pull Request and leave a comment summarizing the changes.
5. The supervisor reviews, then clicks Confirm Merge if all is approved.
Keeping Your Branch Up-to-Date: To sync with the latest changes from the main branch, run: git merge main

After doing this, resolve any conflicts, commit the changes, and continue developing with the latest code base.

These steps will help minimize merge issues and keep everyone’s branches organized!