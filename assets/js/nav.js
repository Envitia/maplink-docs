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
