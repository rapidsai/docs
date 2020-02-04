---
layout: default
title: Home
nav_order: 1
permalink: /
description: |
  This site serves as a collection of all the documentation for RAPIDS. Whether you're new to RAPIDS, looking to contribute, or are a part of the RAPIDS team, the docs here will help guide you.
---

# RAPIDS Docs

{: .fs-8 }

This site serves as a collection of all the documentation for RAPIDS. Whether you're new to RAPIDS, looking to contribute, or are a part of the RAPIDS team, the docs here will help guide you. Visit [rapids.ai](http://rapids.ai) for more information on the overall project.
{: .fs-6 .fw-300 }

[<i class="far fa-file-code"></i> Documentation]({{site.url}}{{site.baseurl}}/api){: .btn .btn-primary .fs-4 .mb-4 .mb-md-0 .mr-2 } [<i class="fas fa-bolt"></i> Get Started]({{site.url}}{{site.baseurl}}/start){: .btn .fs-4 .mb-4 .mb-md-0 .mr-2 } [<i class="fab fa-github"></i> RAPIDS on GitHub](https://github.com/rapidsai){: .btn.fs-4 .mb-4 .mb-md-0 .mr-2 }

---

## Stay Connected

<div class="footer-help-section">
    {% for i in site.social %}
        {% assign social = i[1] %}
        <div class="footer-help-box">
            <div class="footer-help-box-image"><i class="{{ social.fa-icon-class }} fa-3x"></i></div>
            <a href=" {{ social.url }}" target="_blank" class="btn">{{ social.name }}</a>
        </div>
    {% endfor %}
</div>

## Issues or Feedback

[File an issue](https://github.com/rapidsai/docs/issues/new) for any unexpected problems encountered or general feedback with any of the information on this site.
