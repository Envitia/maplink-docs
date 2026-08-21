---
title: "MapLink Pro 11.3 Releases"

releases:
 -  version: 11.3.3
    date: August 21 2026
    summary: CVE remediations.
    sbom: envitia-maplinkpro-11.3.3.cdx.json
 
 -  version: 11.3.2
    date: July 29 2026
    summary: Update of Tracks and DDO SDKs to work with the new cross-platform Skia Drawing Surface.    
    sbom: ../no-sbom

 -  version: 11.3.1
    date: June 25 2026
    summary: Early release of Cross-platform Drawing Surface.   
    sbom: ../no-sbom
---

# MapLink Pro 11.3 Releases

| Version | Release Date  | Summary | Release Notes | SBOM |
| --- | --- | --- | --- | --- |
{% for release in page.releases %}| **{{ release.version }}** | {{ release.date }} | {{ release.summary }} | [Release Notes]({{ release.version }}) | [SBOM]({{ release.sbom }}) |
{% endfor %}
