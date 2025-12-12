---
releases-11: 
 -  version: 11.2.4
    date: December 12 2025
    summary: Bug fixes.
 -  version: 11.2.3
    date: October 10 2025
    summary: Bug fixes.
    release-notes: 11.2/11.2.3
 -  version: 11.2.2
    date: August 22 2025
    summary: Bug fixes.
    release-notes: 11.2/11.2.2
 -  version: 11.2.1
    date: July 21 2025
    summary: Wrap-around maps.
    release-notes: 11.2/11.2.1 
 -  version: 11.1.2
    date: May 12 2025
    summary: Upgrade of Tracks, Network, DDO, Legacy 3D SDKs, merged Spatial (LandLink) into Editor SDK, upgrade DBDB filter.
    release-notes: 11.1/11.1.2
 -  version: 11.1.1
    date: February 20 2025
    summary: Full support for contemporary Windows & Linux OS, compilers and IDEs. Fully updated third-party dependencies. New developer site.
    release-notes: 11.1/11.1.1

releases-10:
 -  version: 10.2.9.42
    date: November 11 2025
    summary: Linux 32-bit release only. Fixed a memory leak in SLD management.
    release-notes: 10.2/10.2.9.42
---

# MapLink Pro 11 Releases

| Version | Release Date  | Summary | Release Notes |
| --- | --- | --- | --- |
{% for release in page.releases-11 %}| **{{ release.version }}** | {{ release.date }} | {{ release.summary }} | [Release Notes]({{ release.release-notes }}) |
{% endfor %}

# MapLink Pro 10 Releases

| Version | Release Date  | Summary | Release Notes |
| --- | --- | --- | --- |
{% for release in page.releases-10 %}| **{{ release.version }}** | {{ release.date }} | {{ release.summary }} | [Release Notes]({{ release.release-notes }}) |
{% endfor %}
