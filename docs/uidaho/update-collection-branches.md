# Update Collection Branches

## Update main!

First, always make sure your `main` branch is up-to-date.
Make sure you are on the `main` branch, then do a `git pull`.

## Start merging updates

Second, start merging the updates into your collection branch:

- Checkout the collection branch to work on, `git checkout psychiana`
- Make sure the branch is updated from GitHub, `git pull`
- Merge main into the collection branch, `git merge main` (this will pull the main branch into the currently checked out branch)
- This merge will result in a bunch of changes and potentially a few conflicts. 
    - If there are no conflicts, the merge will complete automatically. You don't need to do anything else--just start working (and remember to `git push`)!
    - If you have conflicts the auto-merge will not complete--git will leave you in "merging" state until you sort out the conflicts and commit. See further steps below to carefully sort out the merge!

## Sort out merge conflicts

Open the project in VS Code.
Check your "Git" panel on VS Code, you will see all the successful changes as "Staged Changes" (ready to commit), and the conflicts as "Merge changes" (need to be fixed before commit).

If you click one of the files with a conflict, you will see the specific conflict areas highlighted, including the old and new content that conflicts. 
VS Code or GitHub Desktop offer tools to try to manage these conflicts, however you might just want to sort it out manually.
The "HEAD" is the current content, what you have in the branch--generally if there is a conflict, the collection branch has some customized files and you will want to keep the HEAD/current version. 
However, you will often need to carefully check to see if something is updated in `main` that should still be added to the collection branch.
 
Git directly marks the conflicts in the text file by adding a pattern:

- The top of the conflict has `<<<<<<< HEAD` on its own line, followed by the content in the old version of the file. 
- Next you will see a line of `=======`, followed by the content of the new version of the file. 
- Finally closed by `>>>>>>> branch_name`.

These marks are just new normal text characters added to the file to mark the conflicts (any magical buttons around those marks are added by Code or GitHub Desktop and aren't part of Git). 
You could just commit it like that (in which case those marks are just a normal part of the file now) and sort it out later.
I usually just start manually editing the file, and as a final step manually delete the conflict markers. 

Once you sort out the conflicts on a file, on Code's Git menu you can click the plus sign to move the file from "Merge changes" to "Staged changes" so that it is ready to commit.
At that point you can always click on the "Stages changes" to see the git diff visualized, so you can review the changes to make sure they are correct.

The key is to very carefully look at the conflicting files to ensure you are not losing any customization. 

### Test and Check Customizations

At this point the collection should be fully functional, so try `bundle exec jekyll s`. 
Explore over the collection to make sure things seem to be working.
Visit the current digital collection website on the live web to compare.

Each collection might have a number of other small customizations.
Review the features to ensure you aren't over writing these customizations. 
These would most likely be in the pages/ and _layouts. 

### Commit

If everything seems to be working and looks correct, you can finally commit all the changes to complete the merge. 
Making the commit ends the "Merging" status, and you can proceed as normal.
Remember to `git push` your changes.
