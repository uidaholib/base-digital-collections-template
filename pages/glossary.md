---
title: Glossary
layout: page #about
permalink: /glossary.html
# include CollectionBuilder info at bottom
#credits: true
# Edit the markdown on in this file to describe your collection
# Look in _includes/feature for options to easily add features to the page
---

## Pictorial Glossary of Terms

Definitions taken from the USDA [*Glossary of Terms Used in Timber Harvesting and Forest Engineering*](https://www.srs.fs.usda.gov/pubs/gtr/uncaptured/gtr_so073.pdf)

<div class="glossary-container">
{% for t in site.data.timber-glossary %}
<div class="glossary-row">
    <div class="glossary-term">
      <h3 id="{{ t.term | slugify }}">{{ t.term }}</h3>
      <ul>{% assign defs = t.definition | split: '|' %}{% for d in defs %}
        <li>{{ d }}</li>{% endfor %}
      </ul>
    </div>
    <div class="glossary-image">
      {% include feature/image.html objectid=t.images width="75" %}
    </div>
</div>{% endfor %}
