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
  // navtree.js calculates heights from #top.height alone and doesn't know about
  // our 64px site nav. Run after navtree.js (jQuery ready queue is ordered) to
  // correct heights and re-scroll any hash anchor to its proper position.
  if (typeof page_layout !== 'undefined' && page_layout === 1 && typeof $ === 'function') {
    var SITE_NAV_H = 64;

    function fixCppDoxygenLayout() {
      var navTree    = document.getElementById('nav-tree');
      var sideNav    = document.getElementById('side-nav');
      var docContent = document.getElementById('doc-content');
      var topEl      = document.getElementById('top');
      if (!navTree || !sideNav || !topEl) return;

      var topH   = topEl.offsetHeight;        // actual measured titlearea height
      var totalH = SITE_NAV_H + topH;

      // navtree.js over-allocated by SITE_NAV_H — subtract it back
      var ntH = navTree.offsetHeight;
      var snH = sideNav.offsetHeight;
      if (ntH > SITE_NAV_H) navTree.style.height  = (ntH - SITE_NAV_H) + 'px';
      if (snH > SITE_NAV_H) sideNav.style.height  = (snH - SITE_NAV_H) + 'px';
      if (docContent) {
        var dcH = docContent.offsetHeight;
        if (dcH > totalH) docContent.style.height = (dcH - totalH) + 'px';
      }

      // Also set margins dynamically so they match the actual titlearea height
      navTree.style.marginTop = topH + 'px';
      var mainNav = document.getElementById('main-nav');
      if (mainNav) mainNav.style.setProperty('margin-top', totalH + 'px', 'important');

      // Move search box from titlearea into main-nav (matching .NET layout)
      var searchBox = document.getElementById('MSearchBox');
      if (searchBox && mainNav && !mainNav.contains(searchBox)) {
        mainNav.appendChild(searchBox);
        searchBox.style.cssText += ';float:right;margin:4px 12px 4px 0;';
      }

      // Re-scroll to hash anchor now that heights are correct
      var hash = window.location.hash.slice(1);
      if (hash && docContent) {
        var target = document.getElementById(hash);
        if (target) {
          var $dc  = $(docContent);
          var $tgt = $(target);
          var pos  = $tgt.parent().is(':header') ? $tgt.parent().offset().top : $tgt.offset().top;
          var newTop = pos + $dc.scrollTop() - $dc.offset().top;
          if (newTop > 0) $dc.scrollTop(newTop);
        }
      }
    }

    // jQuery processes ready callbacks in registration order. nav.js loads after
    // navtree.js, so our callback runs right after navtree.js's at DOMContentLoaded.
    $(document).ready(fixCppDoxygenLayout);
    $(window).on('resize', function () { setTimeout(fixCppDoxygenLayout, 0); });
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
