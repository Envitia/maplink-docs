(function () {
  var lunrIndex = null;
  var pagesData = [];
  var searchStatus = 'loading'; // 'loading' | 'ready' | 'failed'
  var baseUrl = (typeof siteBaseUrl !== 'undefined' ? siteBaseUrl : '').replace(/\/$/, '');

  fetch(baseUrl + '/search.json')
    .then(function (res) {
      if (!res.ok) throw new Error('HTTP ' + res.status);
      return res.json();
    })
    .then(function (data) {
      pagesData = data;
      if (typeof lunr === 'undefined') throw new Error('lunr not available');
      lunrIndex = lunr(function () {
        this.field('title', { boost: 10 });
        this.field('content');
        this.ref('url');
        data.forEach(function (page) { this.add(page); }, this);
      });
      searchStatus = 'ready';
    })
    .catch(function () {
      searchStatus = 'failed';
    });

  function initSearch(inputEl, resultsEl) {
    if (!inputEl || !resultsEl) return;
    var selectedIndex = -1;

    function getItems() {
      return resultsEl.querySelectorAll('.search-result-item');
    }

    function updateSelection() {
      var items = getItems();
      items.forEach(function (item, i) {
        item.classList.toggle('search-result-focused', i === selectedIndex);
      });
      if (items[selectedIndex]) {
        items[selectedIndex].scrollIntoView({ block: 'nearest' });
      }
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

    function runSearch(query) {
      if (searchStatus === 'loading') {
        showStatus('Search index is loading&hellip;');
        return;
      }
      if (searchStatus === 'failed' || !lunrIndex) {
        showStatus('Search is temporarily unavailable.');
        return;
      }
      var results;
      try {
        results = lunrIndex.search(query + '*');
        if (!results.length) results = lunrIndex.search(query);
        if (!results.length && query.length > 3) results = lunrIndex.search(query + '~1');
      } catch (e) {
        try { results = lunrIndex.search(query); } catch (e2) { results = []; }
      }
      renderResults(deduplicateResults(results), query);
    }

    // If a child section (h3) matches, drop its parent h2 entry from results
    // so the more-specific result wins and we don't show both.
    function deduplicateResults(results) {
      var childUrls = {};
      results.forEach(function (r) {
        var hash = r.ref.indexOf('#');
        if (hash !== -1) {
          var base = r.ref.slice(0, hash);
          childUrls[base] = true;
        }
      });
      return results.filter(function (r) {
        // Keep page-level (no anchor) entries only when no child section matched
        if (r.ref.indexOf('#') === -1) return !childUrls[r.ref];
        return true;
      });
    }

    function renderResults(results, query) {
      selectedIndex = -1;
      resultsEl.classList.add('active');
      if (!results.length) {
        resultsEl.innerHTML = '<p class="search-no-results">No results found for &ldquo;' + escapeHtml(query) + '&rdquo;</p>';
        return;
      }
      var html = '';
      results.slice(0, 10).forEach(function (result) {
        var page = pagesData.find(function (p) { return p.url === result.ref; });
        if (!page) return;
        var title = highlight(page.title, query);
        var excerpt = getExcerpt(page.content, query);
        html += '<a class="search-result-item" href="' + page.url + '" tabindex="-1">';
        html += '<h4>' + title + '</h4>';
        if (page.page) {
          html += '<span class="search-result-page">' + escapeHtml(page.page) + '</span>';
        }
        if (excerpt) {
          html += '<p class="search-result-excerpt">' + highlight(escapeHtml(excerpt), query) + '</p>';
        }
        html += '</a>';
      });
      resultsEl.innerHTML = html;
    }

    inputEl.addEventListener('input', function () {
      selectedIndex = -1;
      var query = this.value.trim();
      if (!query || query.length < 2) { closeResults(); return; }
      runSearch(query);
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
        if (selectedIndex === -1) {
          items.forEach(function (item) { item.classList.remove('search-result-focused'); });
        } else {
          updateSelection();
        }
      } else if (e.key === 'Tab') {
        if (!items.length) return;
        e.preventDefault();
        if (e.shiftKey) {
          selectedIndex = selectedIndex <= 0 ? items.length - 1 : selectedIndex - 1;
        } else {
          selectedIndex = (selectedIndex + 1) % items.length;
        }
        updateSelection();
      } else if (e.key === 'Enter') {
        e.preventDefault();
        if (selectedIndex >= 0 && items[selectedIndex]) {
          window.location.href = items[selectedIndex].href;
        }
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

  // Press '/' to focus the search bar (standard docs site shortcut)
  document.addEventListener('keydown', function (e) {
    if (e.key === '/' && document.activeElement !== desktopInput && document.activeElement !== mobileInput) {
      var tag = document.activeElement ? document.activeElement.tagName : '';
      if (tag !== 'INPUT' && tag !== 'TEXTAREA') {
        e.preventDefault();
        if (desktopInput && desktopInput.offsetParent !== null) {
          desktopInput.focus();
        } else if (mobileInput) {
          mobileInput.focus();
        }
      }
    }
  });

  function getExcerpt(content, query, maxLen) {
    if (!content) return '';
    maxLen = maxLen || 130;
    var lower = content.toLowerCase();
    var idx = lower.indexOf(query.toLowerCase());
    var start, end;
    if (idx === -1) {
      start = 0;
      end = Math.min(maxLen, content.length);
    } else {
      start = Math.max(0, idx - 45);
      end = Math.min(content.length, idx + query.length + 85);
    }
    var text = content.slice(start, end).trim();
    return (start > 0 ? '…' : '') + text + (end < content.length ? '…' : '');
  }

  function highlight(text, query) {
    if (!text) return '';
    var decoded = decodeHtml(text);
    var escaped = escapeHtml(decoded);
    var safe = escapeRegex(query);
    return escaped.replace(new RegExp('(' + safe + ')', 'gi'), '<em>$1</em>');
  }

  function decodeHtml(str) {
    var el = document.createElement('textarea');
    el.innerHTML = str;
    return el.value;
  }

  function escapeHtml(str) {
    return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function escapeRegex(str) {
    return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }
})();
