(function () {
  var toggle = document.getElementById('nav-toggle');
  var navLinks = document.getElementById('nav-links');
  var sidebarToggle = document.getElementById('sidebar-toggle');
  var sidebar = document.getElementById('site-sidebar');
  var sidebarClose = document.getElementById('sidebar-close');
  var sidebarOverlay = document.getElementById('sidebar-overlay');

  var base = (typeof siteBaseUrl !== 'undefined' ? siteBaseUrl : '').replace(/\/$/, '');
  var currentPath = window.location.pathname;

  // ── Hamburger (mobile nav) ──────────────────────────────────────────────────
  if (toggle && navLinks) {
    toggle.addEventListener('click', function () {
      navLinks.classList.toggle('open');
    });

    document.querySelectorAll('.has-dropdown > a').forEach(function (link) {
      link.addEventListener('click', function (e) {
        if (window.innerWidth <= 960) {
          e.preventDefault();
          this.parentElement.classList.toggle('open');
        }
      });
    });

    document.querySelectorAll('.nav-links > li:not(.has-dropdown):not(.mobile-search-item) > a').forEach(function (link) {
      link.addEventListener('click', function () {
        navLinks.classList.remove('open');
      });
    });

    document.addEventListener('click', function (e) {
      if (!e.target.closest('.site-nav')) {
        navLinks.classList.remove('open');
      }
    });
  }

  // ── Active nav item highlighting ────────────────────────────────────────────
  document.querySelectorAll('.nav-links > li > a').forEach(function (link) {
    var href = link.getAttribute('href');
    if (!href || href.startsWith('http')) return;
    if (href === base + '/' || href === '/') {
      if (currentPath === href || currentPath === base + '/') {
        link.parentElement.classList.add('active');
      }
      return;
    }
    if (currentPath.startsWith(href)) {
      link.parentElement.classList.add('active');
    }
  });

  // ── C++ Doxygen layout fix ──────────────────────────────────────────────────
  // navtree.js calculates heights using only the Doxygen titlearea (56px) and
  // doesn't know about our injected 64px site nav. Correct heights after it runs.
  if (typeof page_layout !== 'undefined' && page_layout === 1) {
    var SITE_NAV_H   = 64;
    var TITLEAREA_H  = 56; // #projectrow height per Doxygen CSS
    var TOTAL_HDR_H  = SITE_NAV_H + TITLEAREA_H; // 120px

    function fixCppDoxygenLayout() {
      var navTree    = document.getElementById('nav-tree');
      var sideNav    = document.getElementById('side-nav');
      var docContent = document.getElementById('doc-content');
      if (!navTree || !sideNav) return;
      var ntH = navTree.offsetHeight;
      var snH = sideNav.offsetHeight;
      if (ntH > SITE_NAV_H) navTree.style.height   = (ntH - SITE_NAV_H) + 'px';
      if (snH > SITE_NAV_H) sideNav.style.height   = (snH - SITE_NAV_H) + 'px';
      if (docContent) {
        var dcH = docContent.offsetHeight;
        if (dcH > TOTAL_HDR_H) docContent.style.height = (dcH - TOTAL_HDR_H) + 'px';
      }
    }

    // navtree.js uses $(document).ready() = DOMContentLoaded; window.load fires after.
    window.addEventListener('load', function () { fixCppDoxygenLayout(); });
    // On resize navtree.js fires first (attached earlier), our setTimeout runs after.
    window.addEventListener('resize', function () { setTimeout(fixCppDoxygenLayout, 0); });
  }

  // ── Sidebar navigation panel ────────────────────────────────────────────────
  if (!sidebarToggle || !sidebar) return;

  function openSidebar() {
    sidebar.classList.add('open');
    if (sidebarOverlay) sidebarOverlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeSidebar() {
    sidebar.classList.remove('open');
    if (sidebarOverlay) sidebarOverlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  sidebarToggle.addEventListener('click', function () {
    sidebar.classList.contains('open') ? closeSidebar() : openSidebar();
  });

  if (sidebarClose) sidebarClose.addEventListener('click', closeSidebar);

  document.addEventListener('click', function (e) {
    if (sidebar.classList.contains('open') &&
        !sidebar.contains(e.target) &&
        !sidebarToggle.contains(e.target)) {
      closeSidebar();
    }
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && sidebar.classList.contains('open')) closeSidebar();
  });

  // Expand/collapse sidebar sections via the chevron button
  sidebar.querySelectorAll('.sidebar-expand-btn').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      var item = this.closest('.sidebar-has-children');
      if (item) item.classList.toggle('sidebar-open');
    });
  });

  // Mark active sidebar links and auto-expand the matching section
  sidebar.querySelectorAll('.sidebar-link').forEach(function (link) {
    var href = link.getAttribute('href');
    if (!href || href.startsWith('http')) return;
    if (href === base + '/' || href === '/') {
      if (currentPath === href || currentPath === base + '/') link.classList.add('sidebar-active');
      return;
    }
    if (currentPath.startsWith(href)) {
      link.classList.add('sidebar-active');
      var item = link.closest('.sidebar-has-children');
      if (item) item.classList.add('sidebar-open');
    }
  });

  sidebar.querySelectorAll('.sidebar-sublink').forEach(function (link) {
    var href = link.getAttribute('href');
    if (!href || href.startsWith('http')) return;
    if (currentPath === href || (href.length > 1 && currentPath.startsWith(href))) {
      link.classList.add('sidebar-active');
      var item = link.closest('.sidebar-has-children');
      if (item) item.classList.add('sidebar-open');
    }
  });

  // On mobile, close sidebar after navigating
  sidebar.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () {
      if (window.innerWidth <= 960) closeSidebar();
    });
  });
})();
