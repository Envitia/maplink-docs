(function () {
  var sidebar = document.getElementById('toc-sidebar');
  var tocNav = document.getElementById('toc-nav');
  if (!sidebar || !tocNav) return;

  var headings = document.querySelectorAll('.page-content h2, .page-content h3');

  if (headings.length < 2) {
    sidebar.classList.add('hidden');
    return;
  }

  var items = [];

  headings.forEach(function (h) {
    if (!h.id) {
      h.id = h.textContent.trim().toLowerCase()
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/^-|-$/g, '');
    }
    var a = document.createElement('a');
    a.href = '#' + h.id;
    a.textContent = h.textContent;
    a.className = h.tagName === 'H3' ? 'toc-h3' : 'toc-h2';
    // No preventDefault — browser handles smooth scroll + scroll-margin-top natively
    tocNav.appendChild(a);
    items.push({ el: h, link: a });
  });

  // Scroll spy: highlight the current section as user scrolls
  var activeLink = null;

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        if (activeLink) activeLink.classList.remove('toc-active');
        var match = items.find(function (i) { return i.el === entry.target; });
        if (match) {
          match.link.classList.add('toc-active');
          activeLink = match.link;
        }
      }
    });
  }, { rootMargin: '-64px 0px -70% 0px', threshold: 0 });

  items.forEach(function (item) { observer.observe(item.el); });
})();
