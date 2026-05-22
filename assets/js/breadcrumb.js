(function () {
  var container = document.getElementById('breadcrumb');
  if (!container) return;

  function esc(str) {
    return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  var base = (typeof siteBaseUrl !== 'undefined' ? siteBaseUrl : '').replace(/\/$/, '');
  var path = window.location.pathname;

  if (base && path.startsWith(base)) {
    path = path.slice(base.length);
  }

  path = path.replace(/^\/|\/$/g, '');

  if (!path) return;

  var segments = path.split('/').filter(Boolean);

  // Map URL segments to display names; null = skip the segment entirely
  var nameMap = {
    'pages':       null,
    'support':     'Support',
    'releases':    'Releases',
    'features':    'Features',
    'tutorials':   'Tutorials',
    'api':         'API Docs',
    'cpp':         'C++',
    'dotnet':      '.NET',
    'licences':    'Licences',
    'studio':      'Studio',
    'pdf':         'Documents',
    'sdk-support': 'SDK Support',
    // Developer's Guide pages
    'developers-guide':       "Developer's Guide",
    'introduction':           'Introduction',
    'sdk-components':         'SDK Components and Concepts',
    'basic-applications':     'Basic MapLink Applications',
    'development-environment':'Development Environment',
    'deployment':             'Deployment',
    'samples':                'Samples',
    'walkthrough-1':          'Walkthrough 1 - Your First MapLink Application',
    'walkthrough-2':          'Walkthrough 2 - Modifying the Visible Area',
    'walkthrough-3':          'Walkthrough 3 - Adding a Simple Vector Overlay',
    'geometry-and-overlays':  'Geometry and Overlays',
    'advanced-features':      'Advanced Features',
    'unicode':                'Unicode',
    'opengl-drawing-surface': 'OpenGL Drawing Surface',
    'direct-import-sdk':      'Direct Import SDK',
    'tracks-sdk':             'Tracks SDK',
    'ddo-sdk':                'DDO SDK',
    'terrain-sdk':            'Terrain SDK',
    'maplink-3d-earth-sdk':   'MapLink 3D Earth SDK',
    'editor-sdk':             'Editor SDK',
    'geopackage-sdk':         'GeoPackage SDK',
    'owscontext-sdk':         'OWSContext SDK',
    'ogc-services-sdk':       'OGC Services SDK',
    'spatial-sdk':            'Spatial SDK',
    'gml-sdk':                'GML SDK',
    'net-sdks':               '.NET SDKs',
    'camera-manager':         'Camera Manager',
    'floating-point':         'Floating Point',
    'other-sdks':             'Other SDKs',
    'threading':              'Threading',
    'digm-to-tmf':            'DIGM to TMF Conversion',
  };

  var crumbs = [{ label: 'Home', url: base + '/' }];
  var builtPath = base;

  segments.forEach(function (seg, i) {
    builtPath += '/' + seg;
    var label = Object.prototype.hasOwnProperty.call(nameMap, seg) ? nameMap[seg] : undefined;

    if (label === null) return; // skip structural segments like "pages"

    if (label === undefined) {
      // Format: hyphens → spaces, title case
      label = decodeURIComponent(seg).replace(/\.html?$/i, '').replace(/-/g, ' ').replace(/\b\w/g, function (c) { return c.toUpperCase(); });
      label = label
        .replace(/\bSdk\b/g, 'SDK').replace(/\bSdks\b/g, 'SDKs')
        .replace(/\bOpengl\b/g, 'OpenGL')
        .replace(/\bOgc\b/g, 'OGC')
        .replace(/\bGml\b/g, 'GML')
        .replace(/\bDdo\b/g, 'DDO')
        .replace(/\bTmf\b/g, 'TMF')
        .replace(/\bDigm\b/g, 'DIGM')
        .replace(/\bMaplink\b/g, 'MapLink')
        .replace(/\b3d\b/gi, '3D')
        .replace(/\bGeopackage\b/g, 'GeoPackage')
        .replace(/\bOwscontext\b/g, 'OWSContext')
        .replace(/\bApi\b/g, 'API');
    }

    crumbs.push({ label: label, url: builtPath });
  });

  if (crumbs.length <= 1) return;

  var html = '';
  crumbs.forEach(function (crumb, i) {
    var isLast = i === crumbs.length - 1;
    if (isLast) {
      html += '<span class="bc-current">' + esc(crumb.label) + '</span>';
    } else {
      html += '<a href="' + esc(crumb.url) + '">' + esc(crumb.label) + '</a>';
      html += '<span class="bc-sep">›</span>';
    }
  });

  container.innerHTML = html;
})();
