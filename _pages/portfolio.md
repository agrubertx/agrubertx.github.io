---
layout: archive
title: "Gallery"
permalink: /portfolio/
author_profile: true

gallery:
  - url: ../images/try2.png
    image_path: ../images/try2.png
    alt: "placeholder image 1"
    width: "100px"
    height: "100px"
    title: "Image 1 title caption"
  - url: ../images/testtt.png
    image_path: ../images/testtt.png
    alt: "placeholder image 2"
    title: "Image 2 title caption"
  - url: ../images/nutorus0.svg
    image_path: ../images/nutorus0.svg
    width: "100px"
    height: "100px"
    alt: "placeholder image 3"
    title: "Image 3 title caption"
---
Some pictures
======
{% include gallery caption="This is a sample gallery with **Markdown support**." %}

Some assorted videos
======
[Almost-isometric Willmore flow of a trefoil knot](../videos/knotT.mp4)

[Almost-isometric Willmore flow of a (3,4)-torus knot](../videos/superknotT.mp4)

[MCF of a Moai statue](../videos/MCF_statue.mp4)

[Volume-preserving Willmore flow of a rabbit-dog](../videos/dogtoballV.mp4)

[Volume/Area constrained Willmore flow of a rabbit-dog](../videos/dogtodisk.mp4)

[4-Willmore flow of a cube](../videos/slowgrow.mp4)

[Area-constrained Willmore flow of a cow](../videos/areaprescow.mp4)


{% include base_path %}

{% for post in site.portfolio %}
  {% include archive-single.html %}
{% endfor %}
