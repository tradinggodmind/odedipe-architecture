# Odedipe Michael — Architectural Visualisation

An editorial portfolio of fifteen architectural concept studies, with sixty finished exterior/interior visualisations, fifteen charcoal perspectives, fifteen general-arrangement drawing studies, and individual image captions.

**Portfolio:** https://tradinggodmind.github.io/odedipe-architecture/  
**Contact:** odedipeoluwafemi@gmail.com

## Preview locally

Run `python3 -m http.server 8000` from this directory and open `http://localhost:8000`. No dependencies or build server are needed to serve the site.

## Edit and rebuild

Project descriptions, captions and image sources live in `content/projects.json`. Portrait sources live in `content/portrait.json`. After edits, run:

```sh
python3 tools/build.py
python3 tools/check.py
```

Layouts and behavior live in `style.css`, `app.js` and `loader.js`. Commit the generated HTML alongside the source files. GitHub Pages serves the `main` branch from the repository root; `.nojekyll` preserves the static export.

## Design and delivery

The reference studies in `research/` document Belgrade Arbor, BCG Building Design and SANTAL. The portfolio applies their image-led composition, editorial pacing and grid discipline to an original design. Proprietary reference-site source and assets are excluded.

The site uses responsive AVIF photography with WebP fallbacks, eager loading for the hero, native lazy loading below the fold, intrinsic image dimensions, self-hosted WOFF2 fonts and reduced-motion support. JavaScript handles the entry screen, navigation dialog, project filters and keyboard-accessible image gallery. The entry screen uses the opening image and fonts as readiness signals, skips internal project navigation, respects reduced motion and has a bounded fallback. The portrait/about section is omitted. There are no runtime libraries, trackers, WebGL scenes or video backgrounds.

## Project status and rights

All shown projects are unbuilt conceptual visualisations in proposed real-world settings. Drawing PDFs communicate concept arrangements and are not construction documents. Original portfolio imagery and content are reserved to Odedipe Michael. Instrument Serif and Work Sans use the SIL Open Font License; their license texts are included in `assets/fonts/`.
