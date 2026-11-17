---
layout: page
title: Home
permalink: /
banner-featured-image: https://objects.lib.uidaho.edu/martininstitute/pitman-center-international-ballroom-audience-question.jpg
---

<div class="row">
    <div class="col-md-12">
        <div class="card mb-3">
            <div class="card-body">
                <h2 class="card-title h5">Martin Institute Collections</h2>
                <p class="card-text">The University of Idaho's Martin Institute is a teaching, research, and outreach center dedicated to understanding the causes of war, the conditions necessary for peace, and the international system. This site includes information about the institute's Martin Forums and Distinction in International Service Awards. Click on either of the cards below to access a list of forums and awards.</p>
            </div>
        </div>
    </div>
    {% for a in site.data.sub-collections %}
    <div class="col-md-6">
        <div class="card mb-3">
            <div class="card-body">
                <h3 class="card-title h4">{{ a.title }}</h3>
                {% if a.image %}
                <div class="my-2 p-3 text-center"><img class="img-fluid" src="{{ a.image }}" alt="{{ a.title }}"></div>
                {% endif %}
                <p class="card-text">{{ a.description }}</p>
                <hr>
                <p ><a href="{{ a.link | relative_url }}" class="btn btn-clearwater stretched-link">Browse Collection</a></p>
            </div>
        </div>
    </div>
    {% endfor %}
</div>