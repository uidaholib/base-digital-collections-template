---
layout: page
title: Home
permalink: /
---

<div class="row">
    <div class="col-md-12">
        <div class="card mb-3">
            <div class="card-body">
                <h2 class="card-title h5">College of Engineering Repository</h2>
                <p class="card-text">The College of Engineering Repository preserves and offers access to materials related to the college's regular activities. The collection includes student posters from the annual Engineering Design EXPO, Idaho Asphalt Conference programs, and departmental newsletters.</p>
            </div>
        </div>
    </div>
    {% for a in site.data.subcollections %}
    <div class="col-md-4">
        <div class="card mb-3">
            <div class="card-body">
                <h3 class="card-title h4"><a href="{{ a.object_location | relative_url }}" class="text-dark">{{ a.title }}</a></h3>
                {% if a.image_thumb %}
                <p class="text-center">
                    <a href="{{ a.object_location | relative_url }}">
                        <img class="img-fluid" src="{{ a.image_thumb }}" alt="{{ a.title }}">
                    </a>
                </p>
                {% endif %}
                <p class="card-text">{{ a.description }}</p>
                <hr>
                <a href="{{ a.object_location | relative_url }}" class="btn btn-sm btn-light">Browse Collection</a>
            </div>
        </div>
    </div>
    {% endfor %}
</div>