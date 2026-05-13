(function () {
  var lunrIndex = null;
  var pagesData = [];
  var searchStatus = 'loading';
  var baseUrl = (typeof siteBaseUrl !== 'undefined' ? siteBaseUrl : '').replace(/\/$/, '');

  // Split PascalCase/camelCase tokens so TSLMapDataLayer is also indexed as map, data, layer
  var camelCaseSplitter = function (token) {
    var str = token.toString();
    var parts = str
      .replace(/([a-z\d])([A-Z])/g, '$1 $2')
      .replace(/([A-Z]+)([A-Z][a-z])/g, '$1 $2')
      .split(/[\s_]+/)
      .filter(function (s) { return s.length > 1; });
    if (parts.length <= 1) return token;
    var result = [token];
    parts.forEach(function (part) {
      result.push(token.clone().update(function () { return part.toLowerCase(); }));
    });
    return result;
  };
  lunr.Pipeline.registerFunction(camelCaseSplitter, 'camelCaseSplitter');

  fetch(baseUrl + '/search.json')
    .then(function (res) {
      if (!res.ok) throw new Error('HTTP ' + res.status);
      return res.json();
    })
    .then(function (data) {
      pagesData = data;
      if (typeof lunr === 'undefined') throw new Error('lunr not available');
      lunrIndex = lunr(function () {
        this.pipeline.add(camelCaseSplitter);
        this.field('title', { boost: 15 });
        this.field('page', { boost: 5 });
        this.field('section', { boost: 3 });
        this.field('content');
        this.ref('url');
        data.forEach(function (page) { this.add(page); }, this);
      });
      searchStatus = 'ready';
    })
    .catch(function () {
      searchStatus = 'failed';
    });

  function debounce(fn, delay) {
    var timer;
    return function () {
      clearTimeout(timer);
      var args = arguments, ctx = this;
      timer = setTimeout(function () { fn.apply(ctx, args); }, delay);
    };
  }

  function getType(url) {
    if (url.indexOf('/developers-guide') !== -1) return 'guide';
    if (url.indexOf('/releases/') !== -1) return 'release';
    if (url.indexOf('/support/') !== -1) return 'support';
    if (url.indexOf('/api/') !== -1) return 'api';
    return 'docs';
  }

  function typeLabel(type) {
    return { guide: 'Dev Guide', release: 'Release', support: 'Support', api: 'API', docs: 'Docs' }[type] || 'Docs';
  }

  function initSearch(inputEl, resultsEl) {
    if (!inputEl || !resultsEl) return;
    var selectedIndex = -1;

    function getItems() { return resultsEl.querySelectorAll('.search-result-item'); }

    function updateSelection() {
      var items = getItems();
      items.forEach(function (item, i) {
        item.classList.toggle('search-result-focused', i === selectedIndex);
      });
      if (items[selectedIndex]) items[selectedIndex].scrollIntoView({ block: 'nearest' });
    }

    function closeResults() {
      selectedIndex = -1;
      resultsEl.classList.remove('active');
      resultsEl.innerHTML = '';
    }

    function showStatus(msg) {
      selectedIndex = -1;
      resultsEl.classList.add('active');
      resultsEl.innerHTML = '<p class="search-no-results">' + msg + '</p>';
    }

    function buildQuery(query) {
      var words = query.trim().split(/\s+/).filter(Boolean);
      if (words.length === 1) return null; // handled separately
      // Require all words (AND), with wildcard suffix
      return words.map(function (w) { return '+' + w + '*'; }).join(' ');
    }

    function runSearch(query) {
      if (searchStatus === 'loading') { showStatus('Search index is loading&hellip;'); return; }
      if (searchStatus === 'failed' || !lunrIndex) { showStatus('Search is temporarily unavailable.'); return; }

      var words = query.trim().split(/\s+/).filter(Boolean);
      var results = [];

      try {
        if (words.length > 1) {
          // AND with wildcards (all words required)
          var andWild = words.map(function (w) { return '+' + w + '*'; }).join(' ');
          results = lunrIndex.search(andWild);

          // AND without wildcards
          if (!results.length) {
            var andExact = words.map(function (w) { return '+' + w; }).join(' ');
            results = lunrIndex.search(andExact);
          }

          // OR with wildcards (any word)
          if (!results.length) {
            results = lunrIndex.search(words.map(function (w) { return w + '*'; }).join(' '));
          }
        } else {
          results = lunrIndex.search(query + '*');
          if (!results.length) results = lunrIndex.search(query);
          if (!results.length && query.length > 3) results = lunrIndex.search(query + '~1');
        }
      } catch (e) {
        try { results = lunrIndex.search(query); } catch (e2) { results = []; }
      }

      renderResults(deduplicateResults(results), query);
    }

    var debouncedSearch = debounce(runSearch, 200);

    function deduplicateResults(results) {
      var childUrls = {};
      results.forEach(function (r) {
        var hash = r.ref.indexOf('#');
        if (hash !== -1) childUrls[r.ref.slice(0, hash)] = true;
      });
      return results.filter(function (r) {
        if (r.ref.indexOf('#') === -1) return !childUrls[r.ref];
        return true;
      });
    }

    function renderResults(results, query) {
      selectedIndex = -1;
      resultsEl.classList.add('active');

      if (!results.length) {
        resultsEl.innerHTML = '<p class="search-no-results">No results for &ldquo;' + escapeHtml(query) + '&rdquo;</p>';
        return;
      }

      var shown = results.slice(0, 12);
      var countText = results.length === 1
        ? '1 result'
        : (results.length > 12 ? '12 of ' + results.length + ' results' : results.length + ' results');

      var html = '<div class="search-results-header">' + countText + ' for &ldquo;' + escapeHtml(query) + '&rdquo;</div>';

      shown.forEach(function (result) {
        var page = pagesData.find(function (p) { return p.url === result.ref; });
        if (!page) return;

        var type = getType(page.url);
        var title = highlight(escapeHtml(page.title), query);
        var excerpt = getExcerpt(page.content, query);

        // Build breadcrumb: section › page (for h3/h4), or just page (for h2)
        var breadcrumb = '';
        if (page.section && page.page) {
          breadcrumb = escapeHtml(page.section) + '<span class="bc-sep">›</span>' + escapeHtml(page.page);
        } else if (page.page) {
          breadcrumb = escapeHtml(page.page);
        }

        html += '<a class="search-result-item" href="' + page.url + '" tabindex="-1">';
        html += '<div class="search-result-meta">';
        html += '<span class="search-result-type type-' + type + '">' + typeLabel(type) + '</span>';
        if (breadcrumb) html += '<span class="search-result-breadcrumb">' + breadcrumb + '</span>';
        html += '</div>';
        html += '<h4>' + title + '</h4>';
        if (excerpt) html += '<p class="search-result-excerpt">' + highlightWords(escapeHtml(excerpt), query) + '</p>';
        html += '</a>';
      });

      resultsEl.innerHTML = html;
    }

    inputEl.addEventListener('input', function () {
      selectedIndex = -1;
      var query = this.value.trim();
      if (query.length < 2) { closeResults(); return; }
      debouncedSearch(query);
    });

    inputEl.addEventListener('keydown', function (e) {
      if (!resultsEl.classList.contains('active')) return;
      var items = getItems();

      if (e.key === 'ArrowDown') {
        e.preventDefault();
        selectedIndex = Math.min(selectedIndex + 1, items.length - 1);
        updateSelection();
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        selectedIndex = Math.max(selectedIndex - 1, -1);
        if (selectedIndex === -1) items.forEach(function (i) { i.classList.remove('search-result-focused'); });
        else updateSelection();
      } else if (e.key === 'Tab') {
        if (!items.length) return;
        e.preventDefault();
        selectedIndex = e.shiftKey
          ? (selectedIndex <= 0 ? items.length - 1 : selectedIndex - 1)
          : (selectedIndex + 1) % items.length;
        updateSelection();
      } else if (e.key === 'Enter') {
        e.preventDefault();
        if (selectedIndex >= 0 && items[selectedIndex]) window.location.href = items[selectedIndex].href;
      }
    });

    inputEl.addEventListener('focus', function () {
      if (this.value.trim().length >= 2) runSearch(this.value.trim());
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { closeResults(); inputEl.blur(); }
    });

    document.addEventListener('click', function (e) {
      if (!resultsEl.contains(e.target) && e.target !== inputEl) closeResults();
    });
  }

  var desktopInput = document.getElementById('search-input');
  var mobileInput = document.getElementById('search-input-mobile');
  initSearch(desktopInput, document.getElementById('search-results'));
  initSearch(mobileInput, document.getElementById('search-results-mobile'));

  document.addEventListener('keydown', function (e) {
    if (e.key === '/' && document.activeElement !== desktopInput && document.activeElement !== mobileInput) {
      var tag = document.activeElement ? document.activeElement.tagName : '';
      if (tag !== 'INPUT' && tag !== 'TEXTAREA') {
        e.preventDefault();
        if (desktopInput && desktopInput.offsetParent !== null) desktopInput.focus();
        else if (mobileInput) mobileInput.focus();
      }
    }
  });

  // --- Helpers ---

  function stripMarkdown(text) {
    if (!text) return '';
    return text
      .replace(/!\[[^\]]*\]\([^)]*\)/g, '')
      .replace(/\[([^\]]+)\]\([^)]*\)/g, '$1')
      .replace(/^#{1,6}\s+/gm, '')
      .replace(/(\*\*|__)(.*?)\1/g, '$2')
      .replace(/(\*|_)(.*?)\1/g, '$2')
      .replace(/`{1,3}[^`\n]*`{1,3}/g, '')
      .replace(/^\s*[-*+]\s+/gm, '')
      .replace(/^\s*\d+\.\s+/gm, '')
      .replace(/\s+/g, ' ')
      .trim();
  }

  // Find the window in content where query words are most densely clustered
  function getExcerpt(content, query, maxLen) {
    if (!content) return '';
    maxLen = maxLen || 160;
    var clean = stripMarkdown(content);
    var words = query.toLowerCase().split(/\s+/).filter(Boolean);
    var lower = clean.toLowerCase();

    // Collect all hit positions for any query word
    var positions = [];
    words.forEach(function (w) {
      var idx = 0;
      while ((idx = lower.indexOf(w, idx)) !== -1) {
        positions.push(idx);
        idx += w.length;
      }
    });

    if (!positions.length) {
      return clean.slice(0, maxLen).trim() + (clean.length > maxLen ? '…' : '');
    }

    positions.sort(function (a, b) { return a - b; });

    // Find position with highest word density in a maxLen window
    var best = positions[0];
    var bestScore = 0;
    positions.forEach(function (pos) {
      var score = positions.filter(function (p) { return p >= pos && p <= pos + maxLen; }).length;
      if (score > bestScore) { bestScore = score; best = pos; }
    });

    var start = Math.max(0, best - 40);
    var end = Math.min(clean.length, start + maxLen);
    // Snap to word boundaries
    while (start > 0 && clean[start] !== ' ') start--;
    while (end < clean.length && clean[end] !== ' ') end++;

    var excerpt = clean.slice(start, end).trim();
    return (start > 0 ? '…' : '') + excerpt + (end < clean.length ? '…' : '');
  }

  // Highlight each query word individually (not just exact phrase)
  function highlightWords(text, query) {
    var words = query.split(/\s+/).filter(Boolean);
    words.forEach(function (w) {
      var safe = escapeRegex(w);
      text = text.replace(new RegExp('(' + safe + ')', 'gi'), '<em>$1</em>');
    });
    return text;
  }

  function highlight(text, query) {
    if (!text) return '';
    var decoded = decodeHtml(text);
    var escaped = escapeHtml(decoded);
    return highlightWords(escaped, query);
  }

  function decodeHtml(str) {
    var el = document.createElement('textarea');
    el.innerHTML = str;
    return el.value;
  }

  function escapeHtml(str) {
    if (!str) return '';
    return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function escapeRegex(str) {
    return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }
})();
