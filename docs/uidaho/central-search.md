# Search

We have a custom centralized search application "elasticlibrary" at https://digital.lib.uidaho.edu/

This document outlines the process for configuring our digital collections to use the Search app. 
The full technical details are explained in "docs/uidaho/search-json.md".

## Overview 

Data from each individual collection is *optionally* added to the central search Sources using the file "assets/data/search.json", which is configured by "_data/config-search-index.csv".
A search box configured to use the central search is added by opting in by setting `central-search: true` in "_config.yml".

When a collection is under development and going through the QC process, it will NOT be in the Search index and will be using static Lunr search. 
Once the collection is fully QC-ed and ready for public launch, maintainers will go through the process of adding the collection to Search. 

Adding a collection to the central search is three steps:

1. configure "search.json" and deploy.
2. add to Search Sources.
3. opt in to "central-search" to add search box to nav and deploy.

### 1. Configure search.json mapping

The contents of the "search.json" are configured using the file "_data/config-search-index.csv".
**Do not edit the first column** of the config-search-index, it must contain the same set of dublin core fields for every collection. 
The second column "field" should be customized if necessary to match the most relevant column names in the collection metadata, to enable proper mapping of the metadata to the search index.

Carefully review mapping the "config-search-index.csv" and compare with the collection metadata to ensure the most relevant data fields will be used in "search.json".
In cases where the collection metadata is customized beyond the standard template and contains unique fields, you may need to change the mappings. 
Be thoughtful about which fields should be mapped to provide valuable search to users.
If necessary, do metadata work such as combining or cleaning columns to create the most relevant and useful data.

Ensure the fields meet our standard expectations, since this data will be used in Search and DPLA aggregations. 
In particular check these required standardized fields in the metadata: 

- "title" is not blank.
- "date" is in ISO format (yyyy-mm-dd, yyyy-mm, or yyyy only, no slashes! Other date styles can be in "archival_date" field only).
- "type" matches a standard DCMI Type Vocabulary term.
- "format" matches MIME type standard.
- "rightsstatement" is a valid URI.
- "language" is valid 3 letter code.

#### Full Text search

Consider full text search options for the collection: 

- By default, all items that have a "object_transcript" field in the metadata (usually audio and video items) will have their transcript processed and added to the "search.json" "transcript" field, which will be indexed for full text search. If the transcript should NOT be indexed, add a column named "extract_full_text" and set the value for that item to "false".
- By default all items with "format" `application/pdf` will be marked as a pdf for full text extraction for search.
- If you need to individually exclude some pdf items from text extraction (for example if they don't have text, text is useless/jumbled, there is a "transcript" alternative, or contains potentially sensitive information), add a column "extract_full_text" to the metadata and set it to `false` for the items.
- If the whole collection should *not* default to pdf full text extracted, change the front matter option on "assets/data/search.json" to `pdf-full-text: false`. In this case, you can use a "extract_full_text" column with value `true` to override the default.

#### Excluding Items

By default, all items with an "objectid" and "title" value are included in "search.json" and thus search.
If individual items should be excluded, add a column named "search_index" and give the item the value `false`.

This is sometimes necessary for compound objects where child objects should be excluded or if items contain problematic content unnecessary in search.

#### genre

One special field for search is "genre" as it will displayed at the top of the search listing. 
By default "genre" is mapped to "display_template" which should work for the majority of collections. 

If the collection has odd customized item layouts that won't make sense as a label in that context, do some metadata work to create a new "genre" column that makes sense, then change the mapping in the config.

### 2. Add to Search Sources

When the collection has gone through QC and is ready for public launch, and "search.json" is correctly configured, deploy the collection to it's live web location (or redeploy to ensure "search.json" is up to date). 

Go to the Search Sources page.
Add the full url to the "search.json" and click Add (or if already added, find the entry and click "reindex").

The url follows the pattern:
`https://www.lib.uidaho.edu/digital/collection-stub/assets/data/search.json`

If the index fails, debug the metadata. 

### 3. Opt in to "central-search" 

Once the collection has successfully indexed it will be live in Search.
To add the search box to nav, edit "_config.yml", change the Search Setting option to `central-search: true`.
Save and commit.

Redeploy the collection.

# Default Config

first column of the config should not be modified.

```
dcterm,field
title,title
date,date
creator,creator
description,description
subject,subject
coverage,location
identifier,identifier
source,source
type,type
format,format
language,language
rights,rightsstatement
relation,findingaid
publisher,publisher
genre,display_template
```
