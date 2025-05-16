# Search JSON data

Digital collection data is added to the search index using a standard JSON form prepped for ingest.
In our instance we generate a "search.json" file with each CollectionBuilder digital collection and deploy it with the site. 
However, the json file could be flexibly implemented in other systems (the name and location are arbitrary) following the conventions below.

The list of example "search.json" files is at: 
https://www.lib.uidaho.edu/digital/home/assets/data/search-sources.txt

## Concept

The contents for each item record in "search.json" are modeled on the standard [DCMI core terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) to provide standardized, interoperable data for the search index.
This enables useable search facets and reuse in other platforms.

The "search.json" file is built with each digital collection and exposed on the web. 
The search index application harvests the json to ingest new items or update existing records.
The list of collection json files is used to manage the "Sources" for the search index. 

## Search JSON structure 

The "search.json" file has two main keys, "collection" and "items".

### collection 

The "collection" key contains summary information about the digital collection. 
It is used to set up a collectionObject in the index to connect the individual items with their parent collection.

Required keys:

- "id" - a unique identifier
- "title" - the title of the collection. Will be displayed in Collections facet and with item records in results.

Our implementation of "search.json" contains additional collection information that is not currently used in the Search app. 
We use these additional keys for other data aggregation or for developing new features in the Search app.

Optional keys (not currently used):

- "url" - the full url to the collection's home page.
- "image" - featured image for the collection.
- "description" - description of collection.
- "publisher":
    - "name" - organization title
    - "url" - organization home page
    - "logo" - organization logo image link
- "date_start" 
- "date_end"
- "objects" - keys with counts of unique item formats.
- "data" - url to datapackage.json file
- "last_build_date" - date of deployment

Optional keys are currently ingested into the Search app, but not used.

### items 

The "items" key contains a list of individual records for each item in the digital collection. 
Each item record is a dictionary, with the main keys follow Dublin Core fields, plus a few technical fields used by the Search app.

Required keys: 

- "collectionid" - unique id for the individual digital collection, based on the collection's url slug (baseurl).
- "objectid" - unique id for the item within the collection.
- "url" - full URL to the item's page.

Metadata keys: 

- title - item title, required. Displayed in results.
- date - item date, should be in ISO yyyy-mm-dd, yyyy-mm, or yyyy. Displayed in results. Parsed into date for date range facet.
- creator - multivalued separated by semicolon. Creators facet.
- description - item description. Displayed in results.
- subject - multivalued separated by semicolon. Displayed in results as clickable filters. Subjects facet.
- coverage - location, multivalued separated by semicolon. Locations facet.
- identifier - item identifier used in the organization/source.
- source - citation of item source.
- type - should follow standard DCMI Type Vocabulary.
- format - should follow MIME type standard. Format facet.
- language - should follow 3 letter code.
- rights - valid URI only.
- relation - DC relation. 
- publisher - DC publisher.
- genre - a general genre term. Displayed in results. Genre facet.

Technical keys:

- thumb - full URL to thumbnail image if available (if none, an icon will be used).
- transcript - plain text transcript if available (added to full_text index).
- file - full URL to item download if available.
- extract_full_text - if this key value is `true`, the Search app will try to download the item from the "file" key, extract text, and add to full_text index. This currently only works with PDF files. If this tag is not present, the search will not extract full text (so that PDFs can optionally be excluded).

# CollectionBuilder "search.json" 

At University of Idaho Library, we have a "search.json" implemented in our digital collection templates that is used for the Search app and other metadata aggregation purposes. 
This section describes the specifics of our implementation.

The JSON file is built and deployed with each CollectionBuilder digital collection using a template in "assets/data/search.json"
The mapping between the collection metadata and the "search.json" output is configured in "_data/config-search-index.csv".

## Configure 

The contents of the json are configured using the file "_data/config-search-index.csv".
Custom metadata in each digital collection is mapped to these core fields:
title, date, creator, description, subject, coverage, identifier, source, type, format, language, rights, relation, publisher, genre.

**Do not edit the first column** of the config-search-index, it must contain the same set of dublin core fields for every collection. 
The second column "field" should be customized if necessary to match the most relevant column names in the collection metadata, to enable proper mapping of the metadata to the search index.

In cases where the collection metadata is customized beyond the standard template and contains unique fields, be thoughtful about which fields should be mapped to provide valuable search to users.
If necessary, do metadata work such as combining or cleaning columns to create the most relevant and useful data.

Multiple fields can be mapped to a single dcterm using a semicolon, e.g. `coverage,location;county`.

### genre

One special field for search is "genre" as it will displayed at the top of the search listing. 
By default "genre" is mapped to "display_template" which should work for the majority of collections. 
If the collection has odd customized item layouts that won't make sense as a label in that context, do some metadata work to create a new "genre" column that makes sense, then change the mapping in the config.

### Full Text search

The search index contains a "full_text" field that can be populated from a plain text "transcript" field or by extracting text from a PDF file. 

By default, all items that have a "object_transcript" field in the metadata (usually audio and video items) will have their transcript processed and added to the "search.json" "transcript" field, which will be indexed for full text search. 
If the transcript should NOT be indexed, add a column named "extract_full_text" and set the value for that item to "false".

By default, "search.json" is set to indicate that all items with "format" value of "application/pdf" should be tagged to have their text extracted and entered in full text search.
Individual items can be excluded by using a column named "extract_full_text" and value set to `false`.
Alternatively, if this *should not* be the default for a particular collection, comment out `pdf-full-text: true` in the front matter of the "search.json" file.
Individual items can then be opted in by using a column named "extract_full_text" and value set to `true`.

#### Excluding Items

By default, all items with an "objectid" and "title" value are included in "search.json" and thus search.
If individual items should be excluded, add a column named "search_index" and give the item the value `false`.

This is sometimes necessary for compound objects where child objects should be excluded or if items contain problematic content unnecessary in search.

#### Default Config

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

### Default search.json template

The default CollectionBuilder jekyll template for "search.json" (the template should not be edited or modified):

```
---
# json for ingest into search index
#
# set all PDFs to index full-text?
pdf-full-text: true
# alternatively, use a "extract_full_text" column in the metadata with "true" to select items individually or opt out with "false"
# individual items can be excluded by using a column named "search_index" and value set to "false"
---
{%- assign items = site.data[site.metadata] | where_exp: 'item','item.objectid and item.title and item.search_index != "false"' -%}
{%- assign raw-dates = items | map: 'date' | compact | uniq -%}
{%- capture clean-years -%}{% for date in raw-dates %}{% if date contains "-" %}{{ date | strip | split: "-" | first }}{% elsif date contains "/" %}{{ date | strip | split: "/" | last }}{% else %}{{ date | strip }}{% endif %}{% unless forloop.last %};{% endunless %}{%- endfor -%}{%- endcapture -%}
{%- assign date-range = clean-years | remove: " " | split: ";" | uniq | sort  -%}
{%- assign formats = items | map: 'format' -%}
{%- assign formats_uniq = formats | uniq | compact -%}
{%- assign fields = site.data.config-search-index -%}
{ "collection": {
    "id": "{{ site.baseurl | slugify }}",
    "title": {{ site.title | jsonify }},
    "url": "{{ '/' | absolute_url }}",
    "image": "{{ site.data.featured_item.src | absolute_url }}", 
    "description": {{ site.description | jsonify }},
    {% if site.organization-name %}
    "publisher": { 
        "name": {{ site.organization-name | jsonify }}, 
        "url": "{{ site.organization-link }}", 
        "logo": "{{ site.organization-logo-banner }}" 
    },{%- endif -%}
    "date_start": "{{ date-range | first }}",
    "date_end": "{{ date-range | last }}",
    "objects": { {% for f in formats_uniq %}{% assign count = formats | where_exp: 'i', 'i contains f' | size %}{{ f | jsonify }}: "{{ count }}"{% unless forloop.last %},{% endunless %}{%- endfor -%} },
    "data": "{{ '/assets/data/datapackage.json' | absolute_url }}",
    "last_build_date": "{{ site.time | date: '%Y-%m-%d' }}"
}, 
"items":    
[ {% for item in items %}
    { {% for f in fields %}{% if f.field contains ';' %}{% assign map-fields = f.field | split: ';' %}{% capture map-values %}{% for v in map-fields %}{% if item[v] %}{{ item[v] }};;{% endif %}{% endfor %}{% endcapture %}{% if map-values %}{{ f.dcterm | jsonify }}: {{ map-values | split: ';;' | compact | join: '; ' | jsonify }},{% endif %}{% else %}{% if item[f.field] %}{{ f.dcterm | jsonify }}: {{ item[f.field] | jsonify }}, {% endif %}{%- endif -%}
    {% endfor %}
    {% if item.image_thumb %}"thumb": "{{ item.image_thumb | absolute_url }}", {%- endif -%}
    {% if item.object_transcript and item.extract_full_text != 'false' %}"transcript": {% assign transcript_type = item.object_transcript | slice: 0,1 %}{% if transcript_type == '/' %}{% assign transcript_location = item.object_transcript | remove_first: '/' %}{% assign transcript = site.pages | where: 'path', transcript_location | first %}{{ transcript.content | markdownify | strip_html | normalize_whitespace | jsonify }}{% else %}{{ item.object_transcript | markdownify | strip_html | normalize_whitespace | jsonify }}{% endif %},{%- endif -%}
    {% if item.object_location %}"file": "{{ item.object_location | absolute_url }}", {%- endif -%}
    {% if page.pdf-full-text == true and item.format contains 'pdf' and item.extract_full_text != 'false' %}"extract_full_text": true, {% elsif item.extract_full_text == 'true' %}"extract_full_text": true, {%- endif -%}
    "collectionid": "{{ site.baseurl | slugify }}",
    "objectid": "{% if item.parentid %}{{ item.parentid }}#{% endif %}{{ item.objectid }}",
    "url": "{{ '/items/' | absolute_url }}{% if item.parentid %}{{ item.parentid }}.html#{{ item.objectid }}{% else %}{{ item.objectid }}.html{% endif %}" }{% unless forloop.last %}, {% endunless %}{% endfor %}
]}


```
