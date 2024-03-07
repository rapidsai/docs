---
layout: default
title: Home
nav_order: 1
permalink: /
description: |
  A collection of all the documentation for RAPIDS. Whether you're new to RAPIDS, looking to contribute, or are a part of the RAPIDS team, the docs here will help guide you.
---

# RAPIDS Documentation and Resources
{: .fs-8 }

This site serves to unify the documentation for RAPIDS. Whether you're new to RAPIDS, looking to contribute, or are a part of the RAPIDS team, the docs here will help guide you. Visit [RAPIDS.ai](http://rapids.ai){: target="_blank"} for more information on the overall project.
{: .fs-6 .fw-300 }

## Sections

[<i class="fa-solid fa-download"></i> Installation Guide]({% link install/install.md %}){: .btn.fs-4 .mb-4 .mb-md-4 .mr-2 }
[<i class="fa-solid fa-file-circle-info"></i> User Guides]({% link user-guide/user-guide.md %}){: .btn.fs-4 .mb-4 .mb-md-4 .mr-2 }
<br/>
[<i class="fa-solid fa-file-circle-info"></i> API Documentation]({% link api.md %}){: .btn.fs-4 .mb-4 .mb-md-04 .mr-2 }
[<i class="fa-solid fa-file-circle-info"></i> Visualization Guide]({% link visualization/visualization.md %}){: .btn.fs-4 .mb-4 .mb-md-4 .mr-2 }
<br/>
[<i class="fa-solid fa-file-circle-info"></i> Deployment Guides](/deployment/stable/){: .btn.fs-4 .mb-4 .mb-md-4 .mr-2 }
[<i class="fa-solid fa-file-circle-info"></i> Maintainer Documentation]({% link maintainers/maintainers.md %}){: .btn.fs-4 .mb-4 .mb-md-4 .mr-2 }
<br/>
[<i class="fas fa-bullhorn"></i> RAPIDS Notices]({% link notices/notices.md %}){: .btn.fs-4 .mb-4 .mb-md-4 .mr-2 }
[<i class="fab fa-github"></i> RAPIDS GitHub](https://github.com/rapidsai){: .btn.fs-4 .mb-4 .mb-md-4 .mr-2 }

---

## Stay Connected

<div class="footer-help-section">
    {% for i in site.social %}
        {% assign social = i[1] %}
        <div class="footer-help-box">
            <a href=" {{ social.url }}" target="_blank" class="btn"><i class="{{ social.fa-icon-class }}"></i> {{ social.name }}</a>
        </div>
    {% endfor %}
</div>

## Docs Issues or Feedback

[File an issue](https://github.com/rapidsai/docs/issues/new) for any unexpected problems encountered, incorrect information, or general feedback for this documentation site.
