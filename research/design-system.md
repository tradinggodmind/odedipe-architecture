# Odedipe Michael - portfolio design and implementation

## The creative premise

The portfolio is an architectural publication with a personal point of view. A single complete image establishes presence. A compact identity and a large serif statement introduce the author. The work then opens into a numbered, asymmetrical collection with enough context to make each image meaningful. Its intended response is confidence in Michael's visual judgment, followed by a project enquiry.

The website presents conceptual work honestly. It does not invent built commissions, clients, awards, staff, an office address, engineering credentials or testimonials. The contact destination is the supplied professional email. The portrait/about section was removed at the owner’s request on 8 November 2026; the primary navigation now contains Work, Approach and Contact.

## Reference synthesis

| Reference | Principle retained | Translation into this site |
|---|---|---|
| Belgrade Arbor | An immersive first image and editorial scale contrast | One eager-loaded exterior, large serif display, quiet navigation and a deep-green index panel |
| BCG Building Design | Calm project storytelling and image-led evidence | Individual static case studies, deliberate exterior-to-interior sequence, material notes and captions |
| SANTAL | A precise shared grid and a strong sense of authorship | Repeated rules, small project numbers, aligned metadata and large changes in scale |
| All three | A clear next action | Project links, an accessible gallery, a return to the index, then direct email contact |

The references have different business models. Arbor helps select property. BCG sells a residential design relationship. SANTAL communicates a multidisciplinary practice. Michael sells a visual interpretation of architecture. The final content and interaction scope follow that purpose.

## Visual rules

The page field is #EFEEE7, with #293028 ink, #303D32 dark sections and #62685D supporting text. #DBE5A8 is a limited interactive highlight. Fine rules use #C6C9BC. The palette sits comfortably beside the approved renders without recoloring them.

Instrument Serif supplies display headlines and occasional italic emphasis. Work Sans supplies captions, navigation and body text. The fonts are self-hosted WOFF2, with accompanying SIL Open Font License files. Their combined file size is approximately89KiB. The system uses expressive typographic scale but limits the number of families and weights.

Desktop margins grow from22px to72px. The index uses twelve columns with alternating7/5 and5/7 project spans. Portrait tower images retain a tall presentation. On mobile the cards stack, the header becomes compact, the hero typography reflows, and case-study metadata becomes a readable sequence. Fine type supports the work rather than competing with it.

The full-screen hero uses the Cala Shell exterior. This image has both a recognisable architectural silhouette and a real-world landscape. Its caption identifies the project and proposed setting. A later full-width foyer image changes the rhythm from exterior collection to interior atmosphere before the process section and direct contact.

## Project content model

Each of the15 projects has its own static route, overview, proposed location, typology and six captioned visual studies. The sequence comprises principal exterior, companion exterior, principal interior, companion interior or spatial view, charcoal sectional perspective and general arrangement. The blueprint remains available as a vector PDF. No generated image substitutes for the exact technical PDF.

Each caption describes the actual view. Materials, furniture, light, landscape and occupied scale are named where they are visible. The two drawing captions explain their purpose. Concept status appears in the case-study metadata and the footer. The drawings are described as visual design studies rather than approved construction documents.

The index is curated for visual rhythm, while the original project numbers remain stable. A category filter reduces the collection to landmarks, towers, villas, duplexes, hotels or houses. The filter updates a live result count. Every image can be inspected in a native dialog with next/previous controls, keyboard arrows, Escape dismissal and an optional detail view.

## Motion and loading

The website uses native scrolling. One-time below-fold reveals use IntersectionObserver with opacity and a small26px translation. Hover zoom is restrained. The hero has a short arrival treatment. At the owner’s request on 8 November 2026, a Belgrade Arbor-inspired entry screen was added: a cream field, gold O/M identity, thin progress rule and serif percentage. The screen waits for the opening image and the display/UI fonts, then lifts away. It runs on a fresh entry or full reload and is skipped during internal project navigation. It never waits for lazy-loaded imagery. Asset failures settle normally; a six-second loading deadline and an independent head-script timeout prevent an indefinite cover. With JavaScript disabled, the cover remains hidden and the content stays readable. Reduced-motion preferences remove the minimum display duration and transition. There are no continuous pointer trails, autoplay videos or WebGL scenes.

The portfolio is static HTML, CSS and a small dependency-free interaction script. Each project page is directly addressable on GitHub Pages and works with normal document navigation. The core content is readable without JavaScript. JavaScript adds the entry sequence, filtering, menu and enlarged viewing.

## Image strategy

The60 photographic renders have AVIF versions at480px,960px and original maximum width, plus WebP fallbacks. Original widths are1536px for landscape renders and1024px for portrait exteriors. They were not enlarged to an arbitrary2560px target. The charcoal and blueprint images use WebP, with full drawing sheets up to1800px and vector PDF access.

The hero is eager-loaded with high fetch priority. Other imagery is lazy-loaded and carries intrinsic width and height to reserve space. Responsive source selection changes by placement. A tall mobile hero needs more source pixels than a normal390px-wide card because object-fit cover enlarges a landscape image to fill the height. Its source sizing therefore requests the larger master to preserve detail. Ordinary mobile cards use the smaller AVIF variants.

All fonts and images are local assets. There are no third-party analytics, external font calls, trackers or embedded social feeds. Total repository asset size is not the initial page transfer: visitors fetch the page's selected source variants as they need them, and PDFs load only when opened.

## Verification and limits

The build validates all15 project records, all90 image captions, responsive asset references, page headings and local navigation destinations. Browser checks cover the desktop hero, project filtering, a tower case study, gallery sequencing and Escape dismissal. Mobile and tablet compositions are checked inside390px and768px viewport frames. This tests layout behavior, not a physical handset or every browser engine.

Observed fixes include replacing font-dependent arrow glyphs with SVG icons and requesting a sufficiently detailed image for the tall mobile hero. Performance figures are local file measurements. They are not Lighthouse scores, field Core Web Vitals or a guarantee of network speed. A future production audit should measure cold-cache loading on a representative mobile connection after the public site is deployed.

## Maintenance

Project content lives in a JSON manifest. A small Python generator writes the pages, canonical metadata, sitemap and404 page. The published site does not require Python or a server. The owner can update descriptions and captions, rebuild the static pages, and publish them through the repository.

The public repository contains the finished web exports and open-licensed fonts. Research-only copies of the reference websites' source and proprietary assets are excluded. Full-resolution portfolio masters remain separate from web delivery files.
