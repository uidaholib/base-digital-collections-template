---
# create lunr store for search page
---
{% if jekyll.environment == "production" %}{%- assign items = site.data.engrir_iacprograms | concat: site.data.engrir_expoposters | concat: site.data.engrir_newsletters | where_exp: 'item','item.objectid and item.parentid == nil' -%}{% else %}{%- assign items = site.data[site.metadata] | where_exp: 'item','item.objectid and item.parentid == nil' -%}{% endif %}
{%- assign fields = site.data.config-search -%}
var store = [ 
{%- for item in items -%} 
{  
{% for f in fields %}{% if item[f.field] %}{{ f.field | jsonify }}: {{ item[f.field] | normalize_whitespace | replace: '""','"' | jsonify }},{% endif %}{% endfor %} 
"id": {% if item.parentid %}{{ item.parentid | append: '.html#' | append: item.objectid | jsonify }}{% else %}{{item.objectid | append: '.html' | jsonify }}{% endif %}

}{%- unless forloop.last -%},{%- endunless -%}
{%- endfor -%}
];