---
releases: 
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
---

# MapLink Pro Releases

| Version | Release Date  | Summary | Release Notes |
| --- | --- | --- | --- |
{% for release in page.releases %}| **{{ release.version }}** | {{ release.date }} | {{ release.summary }} | [Release Notes]({{ release.release-notes }}) |
{% endfor %}
