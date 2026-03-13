# Collection Update Project 2026

In spring 2026 we added significant updates to the digital collection templates pulled from CB-CSV.
The "main" branch of each template contains the updated code. 
Each collection branch will need to have the updates merged into the branch from main.

Due a few major changes, this merge will require some manual work to ensure everything is correct and that the About page is set up following the new options.

## Merge Process

- switch to "main" branch 
    - `git pull` (to ensure you have most up to date code)
- switch to a collection branch
    - `git pull` (to ensure you have must up to date collection branch data)
    - `git merge main`
- In VS Code, go to the Version Control pane to look at "Merge Changes"
    - These are files that have merge conflicts and can not be automatically merged. (at this point you can ignore the files listed in "Staged Changes", as those do not have any conflicts as are ready to auto merge)
    - You will need to manually review each of the conflicts to figure out the correct code.
    - Most likely conflicts:
        - "theme.yml" - a few options changed, so their maybe some conflicts showing up.
            - `feature-image-alt-text` added, not necessary if using a collection item.
            - `auto-center-map` added, if it should be "true" no changes are necessary.
        - "about.md" - major changes to the options, so every collection will require manual updates. This usually involves copying values from the old jumbotron into the new front matter options.
            - `about-featured-image` - copy the objectid from the feature/jumbotron.html in the current body. 
            - in the current body, delete feature/jumbotron.html and feature/nav-menu.html 
- After resolving merge conflicts, on the VS Code Version Control pane: 
    - Add each file in "Merge Changes" list
    - write a commit message (generally just "merge updates" or what ever the default is)
    - commit
- Manually review, serve site locally and check over pages versus the currently deployed version.
    - Review "about.md" 
        - check the options to ensure the featured image looks correct
        - check over the headings to ensure they follow logical order and are useful to the TOC
    - Review config-browse.csv
        - check that "facet_name" options make sense