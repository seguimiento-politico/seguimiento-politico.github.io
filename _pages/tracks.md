---
title: Compromisos electorales
comments: true
permalink: /tracks/
---

{% assign teasers = site.images_path | append: 'teasers/' %}
{% assign election_tracks = site.data.tracks | where:'group_by', 'legislature' %}
{% assign party_tracks = site.data.tracks | where:'group_by', 'party' %}

<!-- elecciones electorales  -->
<h6 class="border-bottom pb-2">Elecciones</h6>
<div class="row pt-2">
    <div class="container">
        <div class="row row-cols-auto g-2">       
        {% for track in election_tracks %}
            {% if track.draft == true %}
                {% continue %}
            {% endif %}

            {% assign track_data = track %}

            {% assign slug = track_data.name | slugify %}
            
            {% assign teaser = teasers | append: slug | append: '.png' %}     

            {% assign type_label = track_data.items_type | append: 's_label' %}

            <div class="col card me-2 shadow-sm bg-light">
                <a href="/tracks/{{ track_data.name | slugify }}">
                    <img src="{{ teaser }}" alt="{{ case }}">
                </a>
            </div>
        {% endfor %}
        </div>
    </div>
</div>
<br>

<!-- programas electorales -->
<h6 class="border-bottom pb-2">Partidos</h6>
<div class="row pt-2">
    <div class="container">
        <div class="row row-cols-auto g-2">       
        {% for track in party_tracks %}
            {% if track.draft == true %}
                {% continue %}
            {% endif %}

            {% assign track_data = track %}

            {% assign slug = track_data.name | slugify %}
            
            {% assign teaser = teasers | append: slug | append: '.png' %}     

            {% assign type_label = track_data.items_type | append: 's_label' %}

            <div class="col card me-2 shadow-sm bg-light">
                <a href="/tracks/{{ track_data.name | slugify }}">
                    <img src="{{ teaser }}" alt="{{ case }}">
                </a>
            </div>
        {% endfor %}
        </div>
    </div>
</div>

