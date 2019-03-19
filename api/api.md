---
layout: default
title: API Docs
nav_order: 2
has_children: false
permalink: api
---

# API Docs
{:.no_toc}

Access our current "stable" API docs for all RAPIDS libraries below. In addition, explore our "nightly" docs containing the latest features and updates for the next release.
{: .fs-6 .fw-300 }

{% for lib in site.data.apis %}
{% assign api = lib[1] %}
### {{ api.name }} 
#### [stable]({{ site.url }}{{ site.baseurl }}/api/{{ api.path }}/stable) | [nightly]({{ site.url }}{{ site.baseurl }}/api/{{ api.path }}/nightly) | [github](https://github.com/rapidsai/{{ api.path }}){:target="_blank"}
{{ api.desc }}
{% endfor %}