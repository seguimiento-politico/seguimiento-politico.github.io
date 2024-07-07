---
title: Todas las temáticas
comments: true
permalink: /topics/
---

<!-- all statements -->
<!-- TODO: Add page_sequence into statements data for finer ordering -->
{% assign items = site.data.topics %}
{% assign total = items  | size %}

{{content}}

<!-- TODO: {% include categorization.html filter1='parties' filter2='topic' %} -->

{% include categorization.html type='parties' %}
