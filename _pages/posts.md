---
layout: archive
permalink: /posts/
title: "Blog Posts"
author_profile: false
---

{% include base_path %}
{% capture written_year %}'None'{% endcapture %}
{% for post in site.posts %}

  {% include archive-single.html %}
{% endfor %}
