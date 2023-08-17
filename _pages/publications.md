---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: false
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="https://scholar.google.com/citations?user=KETTV4YAAAAJ&hl=en">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}


<!-- # Pre-prints

[Waveflow: Enforcing boundary conditions in smooth normalizing flows with application to fermionic wave functions](https://arxiv.org/abs/2211.14839) -->

[Monte-Carlo simulations of spin-crossover phenomena based on a vibronic Ising-like model with realistic parameters](https://pubs.rsc.org/en/content/articlelanding/2015/cp/c4cp05562d/unauth)