---
layout: archive
title: "Gallery"
permalink: /portfolio/
author_profile: true

gallery:
  - url: /assets/images/unsplash-gallery-image-1.jpg
    image_path: /assets/images/unsplash-gallery-image-1-th.jpg
    alt: "placeholder image 1"
    title: "Image 1 title caption"
  - url: /assets/images/unsplash-gallery-image-2.jpg
    image_path: /assets/images/unsplash-gallery-image-2-th.jpg
    alt: "placeholder image 2"
    title: "Image 2 title caption"
  - url: /assets/images/unsplash-gallery-image-3.jpg
    image_path: /assets/images/unsplash-gallery-image-3-th.jpg
    alt: "placeholder image 3"
    title: "Image 3 title caption"
---

{% include gallery caption="This is a sample gallery with **Markdown support**." %}

[Almost-isometric Willmore flow of a trefoil knot](videos/knotT.mp4)

[Almost-isometric Willmore flow of a (3,4)-torus knot](videos/superknotT.mp4)

<a href="videos/MCF_statue.mp4" >MCF of a Moai statue</a></li>

<a href="videos/dogtoballV.mp4" >Volume-preserving Willmore flow of a rabbit-dog</a></li>

<a href="videos/dogtodisk.mp4" >Volume/Area constrained Willmore flow of a rabbit-dog</a></li>

<a href="videos/slowgrow.mp4" >4-Willmore flow of a cube</a></li>

<a href="videos/areaprescow.mp4" >Area-constrained Willmore flow of a cow</a></li>


{% include base_path %}


{% for post in site.portfolio %}
  {% include archive-single.html %}
{% endfor %}
