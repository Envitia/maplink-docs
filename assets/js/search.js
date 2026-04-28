(function () {
  var input = document.getElementById("site-search-input");
  var resultsContainer = document.getElementById("site-search-results");

  if (!input || !resultsContainer) {
    return;
  }

  var searchIndex = [];
  var maxResults = 10;
  var searchPath = (window.location.pathname.indexOf("/maplink-docs/") === 0)
    ? "/maplink-docs/search.json"
    : "/search.json";

  function escapeHtml(text) {
    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/\"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  function renderResults(items) {
    if (!items.length) {
      resultsContainer.innerHTML = '<p class="top-nav__search-empty">No matches found.</p>';
      resultsContainer.classList.add("is-open");
      return;
    }

    var listHtml = items
      .map(function (item) {
        var snippet = item.content.slice(0, 140);

        return [
          '<a class="top-nav__search-result" href="' + escapeHtml(item.url) + '">',
          '<strong>' + escapeHtml(item.title) + '</strong>',
          '<span>' + escapeHtml(snippet) + '</span>',
          '</a>'
        ].join("");
      })
      .join("");

    resultsContainer.innerHTML = listHtml;
    resultsContainer.classList.add("is-open");
  }

  function clearResults() {
    resultsContainer.classList.remove("is-open");
    resultsContainer.innerHTML = "";
  }

  function runSearch(query) {
    var terms = query
      .toLowerCase()
      .split(/\s+/)
      .filter(Boolean);

    if (!terms.length) {
      clearResults();
      return;
    }

    var matches = searchIndex.filter(function (item) {
      var haystack = (item.title + " " + item.content).toLowerCase();
      return terms.every(function (term) {
        return haystack.indexOf(term) !== -1;
      });
    });

    renderResults(matches.slice(0, maxResults));
  }

  var debounceTimer;
  input.addEventListener("input", function (event) {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(function () {
      runSearch(event.target.value);
    }, 120);
  });

  input.addEventListener("focus", function () {
    if (input.value.trim()) {
      runSearch(input.value);
    }
  });

  document.addEventListener("click", function (event) {
    if (!resultsContainer.contains(event.target) && event.target !== input) {
      clearResults();
    }
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      clearResults();
      input.blur();
    }
  });

  fetch(searchPath)
    .then(function (response) {
      if (!response.ok) {
        throw new Error("Search index request failed.");
      }
      return response.json();
    })
    .then(function (data) {
      searchIndex = data || [];
    })
    .catch(function () {
      input.setAttribute("placeholder", "Search unavailable");
    });
})();
