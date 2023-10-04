# Update collection branches

> major update December 2021

## Update main!

First, always make sure your `main` branch is up-to-date, do a `git pull` on main.

## Merge main branch into the branch you've selected

1. In GitHub Desktop, find the branch name that you want to update and switch to it.
2. In the Branches dropdown on GitHub Desktop, click the bottom button that says "Choose a branch to merge into [whatever branch you're on]," and choose the "main" branch. Once you select "main," the merge will begin.
3. In most cases, there will be conflicting files, and you'll need to click a button that accepts this to continue the merge.

## Sort out merge conflicts

GitHub Desktop will list the conflicts you need to resolve before the merge can be committed. To resolve them:

1. Open the project in VS Code and locate and open a file that GitHub desktop says needs to be resolved. 
2. Scroll down in that file until you see the specific conflict area(s) highlighted, including the old and new content that conflicts. Git directly marks the conflicts in the text file by adding a pattern:
    - The top of the conflict has `<<<<<<< HEAD` on its own line, followed by the content in the old version of the file. 
    - Next you will see a line of `=======`, followed by the content of the new version of the file. 
    - Finally closed by `>>>>>>> branch_name`.
3. VS Code offers tools to try to manage these conflicts: above the highlighted section, you'll see a series of buttons that say `accept current change`, `accept incoming change`, and `accept both`. (Note these buttons are added by VS Code and aren't part of Git).
    - `current change` = changes on the current branch
    - `incoming change` = changes from the main branch
4. Which option you accept depends on which file you're looking at, so always look carefully at the code before determining which change to accept. In many cases, if the file is in the _includes folder, you'll probably accept the `incoming change` option to incorporate general updates to the collectionbuilder template code. If the file is in the _data folder, you'd be more likely to accept the `current change`, since these files are likely heavily customized to fit the collection. This isn't always the case, though, so take care and don't hesitate to reach out to Olivia to confirm. In some cases you might need to `accept both` and then sort it out manually.
5. Once you sort out the conflicts on a file, save the file. When you switch back to GitHub Desktop, you should see that the conflict is resolved, so you can move on to the next conflict following the instructions above.
6. Remember that you can always click on the files you edited in the Changes column of VS Code to see the git diff visualized, so you can review the changes to make sure they are correct.
7. After you've sorted out all the conflicts, you can either make a commit or move onto the changes below, whichever makes the most sense to you. If there are a lot of files that were changed in the merge, it might make more sense to commit at this point, since you'll be changing more in the steps below and it may be hard to keep track of your changes.

## Test and Check Customizations

At this point the collection should be fully functional, so try `bundle exec jekyll s`. 
Explore over the collection to make sure things seem to be working.
Visit the current digital collection website on the live web to compare.

Each collection might have a number of other small customizations.
Review the features to ensure you aren't over writing these customizations. 
These would most likely be in the pages/ and _layouts. 

## Commit

If everything seems to be working and looks correct, you can finally commit all the changes to complete the merge. 
Making the commit ends the "Merging" status, and you can proceed as normal.
Remember to `git push` your changes.
