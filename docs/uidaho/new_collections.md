# Steps for Creating a New Collection

## Prep

- Choose the base name for the collection that will become the URL, branch name, and used for objectids. Typically this will be one word, all lowercase, no spaces (can use `-`).
- In your metadata spreadsheet, create objectids for your collection items, using the base name (such as `tabor` for Tabor Photograph Collection) + enough zeros to accommodate the item numbers (ex: `tabor000`)
- Make sure your jpegs and pdfs are all together in one folder, ready to be added to the repository

## Create Derivatives

- Navigate to the [digital-collections-template-cb-csv](https://github.com/uidaholib/digital-collections-template-cb-csv) repo on GitHub
- In the branch dropdown, create a new branch with the base name (`tabor`). Use only lowercase letters for branch name, preferably one word.
- In GitHub Desktop, fetch and pull the changes to the collectionbuilder-csv-template repository.
- Switch to the new branch you just created, and open it in Visual Studio Code.
- In the base of the repository, create an `objects` folder and add the collection's digital objects to it.
- In the terminal, run the command `rake generate_derivatives`. This will create `thumbs` and `small` folders inside your `objects` folder, inside of which you'll find newly-created thumbs and smalls of the collection objects.

## Place Objects on Server

- On the library web server, navigate to /digital/objects/, and create a new folder using the base name (in this case, the folder name is `tabor`).
- Make sure that the `rake generate_derivatives` task is complete before doing the following steps.
- Copy and paste the full sized objects from your repository's `objects` folder into this new `tabor` folder.
- Copy and paste the `thumbs` and `small` folders (along with their new content) from your repository's `objects` folder into the new `tabor` folder.
- Delete the contents of the `objects` folder from your repository (you do NOT commit them to the project!)

## Add Object Paths to Metadata

- Return to your metadata spreadsheet in Google Sheets, and add the following fields if they are not present already: `display_template`, `object_location`, `image_small`, `image_thumb`. Use Google Sheets formulas to fill out these fields based on the objects' formats and their location on the library web server. Use the following resources for help with this:
    - Example metadata (do not edit!): https://docs.google.com/spreadsheets/d/1nN_k4JQB4LJraIzns7WcM3OXK-xxGMQhW1shMssflNM/edit?usp=sharing
    - Metadata Guidelines: https://collectionbuilder.github.io/cb-docs/docs/metadata/csv_metadata/#object-detail-fields-strongly-suggested
