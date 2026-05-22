# maplink-docs

Documentation site for **Envitia MapLink Pro** — a geospatial SDK for building high-performance mapping and situational awareness applications.

**Live site:** [envitia.github.io/maplink-docs](https://envitia.github.io/maplink-docs/)

---

## What's in this repo

This is a [Jekyll](https://jekyllrb.com/) site hosted on GitHub Pages. Content is written in Markdown and organised as follows:

```
maplink-docs/
├── main.md                  # Website homepage (served at /)
├── pages/
│   ├── quick-start-guide.md # Installation and first steps
│   ├── developers-guide.md  # In-depth developer reference
│   ├── docs.md              # Docs index page
│   ├── features/            # Feature-specific pages (e.g. wrap-around maps)
│   ├── releases/            # Release notes per version
│   ├── support/             # Support pages (install, platform, SDK, deployment)
│   └── tutorials/           # Step-by-step tutorials
├── api/
│   ├── cpp/                 # C++ API reference (Doxygen-generated HTML)
│   └── dotnet/              # .NET API reference
├── studio/                  # MapLink Studio documentation
├── licences/                # Third-party licence information
├── _data/
│   ├── nav.yml              # Site navigation structure
│   ├── docs.yml             # Docs index card list
│   └── thirdpartylicences.yml
├── _layouts/                # Jekyll HTML layouts
├── assets/ / css/ / img/    # Static assets
├── pdf/                     # Downloadable PDFs
└── _config.yml              # Jekyll site configuration
```

---

## Running locally

You need Ruby and Bundler installed.

```bash
# Install dependencies
bundle install

# Serve with live reload
bundle exec jekyll serve

# Then open http://localhost:4000/maplink-docs/
```

> The site uses the `github-pages` gem to match the GitHub Pages build environment.

---

## Editing content

All documentation pages are Markdown files. Most have Jekyll front matter at the top:

```yaml
---
title: Page Title
---
```

- **Navigation** is controlled by [_data/nav.yml](_data/nav.yml)
- **Docs index cards** are listed in [_data/docs.yml](_data/docs.yml)
- **Homepage** is [main.md](main.md) (renders at `/`)

### Adding a new page

1. Create a `.md` file in the appropriate `pages/` subdirectory
2. Add front matter (`title` at minimum)
3. If it should appear in the nav, add an entry to `_data/nav.yml`

---

## Contributing

1. Fork the repo and create a branch from `main`
2. Make your changes (Markdown edits, new pages, nav updates)
3. Test locally with `bundle exec jekyll serve`
4. Open a pull request

---

## Platform support

MapLink Pro has C++ and .NET APIs and runs on Windows and Linux. See the [Platform Support page](https://envitia.github.io/maplink-docs/pages/support/platform-support) for details.

## Request a trial

[Apply for a trial licence](https://forms.office.com/e/Lr7jN9TCC0)

## Support

For support queries, email the Envitia support team. See the [support pages](https://envitia.github.io/maplink-docs/pages/support/) for more information.
