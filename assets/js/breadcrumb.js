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
      label = label.replace(/\bSdk\b/g, 'SDK').replace(/\bSdks\b/g, 'SDKs');
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
