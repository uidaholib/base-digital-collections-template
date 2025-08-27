---
title: Glossary
layout: about
permalink: /glossary.html
# include CollectionBuilder info at bottom
credits: true
# Edit the markdown on in this file to describe your collection
# Look in _includes/feature for options to easily add features to the page
---

{% include feature/jumbotron.html objectid="https://objects.lib.uidaho.edu/priestriver/banner.jpg" %}

## Pictorial Glossary of Terms

Definitions taken from the USDA [*Glossary of Terms Used in Timber Harvesting and Forest Engineering*](https://www.srs.fs.usda.gov/pubs/gtr/uncaptured/gtr_so073.pdf)

<div class="glossary-container">
  <div class="glossary-row">
    <div class="glossary-term">
      <strong>Bateau:</strong>
      <ul>
        <li>A flat-bottomed boat with raked bow and stern and flaring sides.</li>
      </ul>
    </div>
    <div class="glossary-image">
      {% include feature/image.html objectid="priestriver0275" width="75" %}
    </div>
  </div>
  <div class="glossary-row">
    <div class="glossary-term">
      <strong>Boom:</strong>
      <ul>
        <li>Pole, timber, or metal arm protruding from a machine; for example, the boom on a loading machine.</li>
        <li>Raft of logs or a loose bag of logs in the water.</li>
        <li>Logs connected together to form a pocket to confine logs into a raft.</li>
      </ul>
    </div>
    <div class="glossary-image">
      {% include feature/image.html objectid="priestriver0260" width="75" %}
    </div>
  </div>
  <div class="glossary-row">
    <div class="glossary-term">
      <strong>Cant Hook:</strong>
      <ul>
        <li>Stout wooden lever used in rolling logs. Differs from a peavey in that it has no spike in the end of the stock.</li>
      </ul>
    </div>
    <div class="glossary-image">
      {% include feature/image.html objectid="priestriver0296" width="75" %}
    </div>
  </div>
  <div class="glossary-row">
    <div class="glossary-term">
      <strong>Crawler:</strong>
      <ul>
        <li>Tractor operating on continuous treads instead of wheels.</li>
      </ul>
    </div>
    <div class="glossary-image">
      {% include feature/image.html objectid="priestriver0419" width="75" %}
    </div>
  </div>
  <div class="glossary-row">
    <div class="glossary-term">
      <strong>Flume:</strong>
      <ul>
        <li>Trough of water used to convey wood.</li>
      </ul>
    </div>
    <div class="glossary-image">
      {% include feature/image.html objectid="priestriver0575" width="50" %}
    </div>
  </div>
  <div class="glossary-row">
    <div class="glossary-term">
      <strong>Jammer:</strong>
      <ul>
        <li>Lightweight, two-drum yarder usually on a truck with a spar and boom; may be used for both short distance yarding and loading.</li>
      </ul>
    </div>
    <div class="glossary-image">
      {% include feature/image.html objectid="priestriver0430" width="50" %}
    </div>
  </div>
  <div class="glossary-row">
    <div class="glossary-term">
      <strong>Peavey:</strong>
      <ul>
        <li>Stout wooden lever, fitted with a strong, sharp spike used for rolling logs.</li>
      </ul>
    </div>
    <div class="glossary-image">
      {% include feature/image.html objectid="priestriver0330" width="75" %}
    </div>
  </div>
  <div class="glossary-row">
    <div class="glossary-term">
      <strong>Rollway:</strong>
      <ul>
        <li>Any place where logs are dumped and they roll or slide to their resting place.</li>
      </ul>
    </div>
    <div class="glossary-image">
      {% include feature/image.html objectid="priestriver0439" width="75" %}
    </div>
  </div>
  <div class="glossary-row">
    <div class="glossary-term">
      <strong>Sorting Gaps:</strong>
      <ul>
        <li>The areas on a log pond enclosed by boom sticks into which logs are sorted.</li>
      </ul>
    </div>
    <div class="glossary-image">
      {% include feature/image.html objectid="priestriver0256" width="75" %}
    </div>
  </div>
  <div class="glossary-row">
    <div class="glossary-term">
      <strong>Splash Dam:</strong>
      <ul>
        <li>A temporary wooden dam used to raise the water level in streams to float logs downstream to sawmills.</li>
      </ul>
    </div>
    <div class="glossary-image">
      {% include feature/image.html objectid="priestriver0289" width="75" %}
    </div>
  </div>
  <div class="glossary-row">
    <div class="glossary-term">
      <strong>Streamside, Green Strip or Buffer Strip:</strong>
      <ul>
        <li>Strip of uncut timber left between cutting units or adjacent to another resource.</li>
      </ul>
    </div>
    <div class="glossary-image">
      {% include feature/image.html objectid="priestriver0422" width="75" %}
    </div>
  </div>
</div>
<style>
.glossary-container {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
.glossary-row {
  display: flex;
  flex-direction: row;
  align-items: center;
  border-bottom: 1px solid #e0e0e0;
  padding-bottom: 1rem;
}
.glossary-term {
  flex: 1;
  padding-right: 1.5rem;
}
.glossary-image {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}
.glossary-term ul {
  margin-top: 0.5rem;
  margin-bottom: 0;
  padding-left: 1.5rem;
}
.glossary-term li {
  margin-bottom: 0.5rem;
}
.glossary-term li:last-child {
  margin-bottom: 0;
}
@media (max-width: 768px) {
  .glossary-row {
    flex-direction: column;
  }
  
  .glossary-term {
    padding-right: 0;
    padding-bottom: 1rem;
  }
}
</style>