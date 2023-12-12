---
title: Resources
layout: page-narrow
permalink: /resources.html
---

# Resources

## Websites 

*Note: most of these links are archived sources from Internet Archive*

{% assign web = site.data.iwi_resources | where: "type","Web Resources" %}
{% for r in web %}- [{{ r.resource }}]({{ r.link }})
{% endfor %}

## Books 

{% assign books = site.data.iwi_resources | where: "type","Books" %}
{% for r in books %}- {{ r.resource }}
{% endfor %}

## Libraries & Archives

{% assign org = site.data.iwi_resources | where: "type","Libraries & Museums" %}
{% for r in org %}- [{{ r.resource }}]({{ r.link }})
{% endfor %}
