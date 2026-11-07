# Architectural website evidence and rebuild notes

Prepared for Odedipe Michael · 7 November 2026

## Scope and confidence

This study directly inspects the current public HTML, CSS and JavaScript of BCG Building Design and SANTAL. It distinguishes source-observed behaviour from inferred design purpose. It does not establish the designers’ private reasoning, verify accessibility end to end or measure real-user performance. Exact source values below are implementation evidence, not recommendations to copy unchanged. Browser inspection also checked the visible composition, navigation and initial scroll states; detailed timings below come from public source declarations.

Primary source URLs and downloaded files are listed at the end. The website assets and fonts remain reference material. They must not be redistributed with Michael’s portfolio.

## BCG Building Design

### Positioning and visitor journey

The site presents a personally led residential design practice. Its route is highly commercial yet visually calm. A large residential image establishes an aesthetic before the visitor reads a studio introduction, selected work, a process explanation, client evidence and the project-enquiry invitation. Separate Studio, Projects, Process, Project Enquiry and Contact pages let a serious visitor investigate beyond the initial impression.

The inferred purpose of this sequence is to connect appearance with delivery confidence. The studio is selling both a desirable home and a guided process. For Michael, the corresponding progression should show image-making quality first, then explain camera, materials and atmosphere through actual project images. It would be inappropriate to import BCG’s construction claims or testimonials.

### Measured visual system

| Role | Source-observed value | Interpretation |
|---|---|---|
| Page field | `--brand--beige: #f3efe8` | A warm paper-like neutral works with pale residential photography. |
| Secondary field and links | `--brand--brown: #3a3028` | Brown gives depth without the harshness of pure black. |
| Alternate white | `--neutral--white: #fffdf8` | Warmth is preserved even in reversed type. |
| Primary ink | `--neutral--black: #1b1a18` | Dense readable text with a warm cast. |
| Additional named accent | `--terracota: #a9645b` | Exists in the system, but its existence does not prove prominent use on every page. |
| Primary type | `NeueHaasDisplay Pro`, Arial, sans-serif | A compact grotesk supplies authority through scale, alignment and weight. |
| Loaded weights | 500, 600 and 700 declarations | Medium and bold roles dominate rather than a large family of styles. |
| H1 token | 3.5rem, line-height .9, weight600 | Tight display typography. Actual component class selection matters more than tag name. |
| Hero visible headline | `heading-style-h3`, 2.5rem, line-height1 | The visible message is deliberately modest against the large image. The page also contains a visually hidden SEO H1. |
| Desktop grid | 12 equal columns, .5rem gap | Explicit alignment, not an arbitrary collage. |
| Maximum hero container | 100rem | Maintains control on very wide monitors. |
| Default horizontal page padding | .69rem | Image-led edge proximity rather than a large conventional marketing margin. |
| Section padding tokens | 2.5 / 5 / 7rem | A controlled rhythm of compact, normal and spacious sections. |

The source also declares several Neue Haas trial font assets. Their presence is not a license for reuse. Michael’s build should use separately licensed or open-licensed fonts.

### Composition and image direction

The hero is a minimum `100svh` container with the text aligned to its lower edge. The photograph sits in an absolutely positioned, full-size background. Its tonal whites, warm timber and planted edges are part of the composition. The headline is subordinate to the built work.

The studio narrative uses a long horizontal presentation. The track is `250vh`; individual cards are `50vw`; a card’s internal frame may extend to `100vw × 100vh`. This is a deliberate reveal of successive editorial panels as the visitor scrolls. Source code moves the row by the measured distance from its end card to the track boundary. It does not assume a hard-coded card count.

Featured work is a vertical list on desktop. The active image is placed over a shared display area and uses a portrait 9:12 ratio with a maximum width of36.63rem. Hover, focus and click update the selected item. This creates visual concentration around one project rather than presenting six competing photographs at once. On touch-sized layouts the design stops relying on hover and exposes the images in a grid or stacked list.

Case studies use a restrained title and metadata area followed by a two-column image grid. The Kembali page contains25 image elements in the captured HTML. A top rule and a .5fr/1fr metadata grid separate labels from values. This gives the image sequence the feel of a project dossier.

### Motion, with exact source evidence

BCG combines Webflow, GSAP3.15.0, ScrollTrigger, SplitText, Lenis and Barba2.10.3. The code directly names all of these dependencies.

- Lenis initialises with `lerp:.1`, `wheelMultiplier:.7`, vertical gestures and `smoothTouch:false`. A requestAnimationFrame loop drives it.
- Shared GSAP defaults are1.6seconds and `sine.inOut`. Individual effects override these.
- Scroll text uses line masks, y translation from100%, .8second `power3.out` reveals and .05second stagger. The trigger begins at the element’s top reaching90% of the viewport.
- The hero introduction uses1second lines with .2second delay, .08second stagger and `power4.out`.
- The preloader has a6second fail-safe hide. Its logo animates through masked, duplicated letter layers before the overlay exits upward in .8seconds.
- Barba page navigation scales the outgoing page by `1 - 96 / viewportWidth`, moves it50px downward and brings in the new page from below. The incoming clip changes from `inset(30% 15% 0% 15%)` to a full rectangle over1.35seconds using `power4.out`.
- Navigation is temporarily locked during the transition, then released. This makes re-entrant clicks less likely but also makes the motion a real interaction cost.
- The footer letters rise from110% with .03second stagger; its rule grows from the left over1second.

Inferred intent is cinematic continuity, a measured reveal and an uninterrupted branded atmosphere. The implementation also reveals the cost of that intent: lifecycle cleanup, script re-initialisation after navigation, image-loading coordination and fallbacks to release locked controls. A lightweight portfolio can reproduce the feeling with smaller opacity/transform effects and ordinary document navigation.

### Responsive logic

CSS includes the common Webflow479,767 and991px maximum-width breakpoints and a1920px wide-screen branch. Custom behaviour uses additional boundaries.

- Below768px the mobile menu uses a clipped full panel, replacing the small desktop links.
- Below768px the featured-image swap is disabled. Images become directly visible.
- From768–1032px, scrolling each project row through70% of the viewport activates its image, supporting tablet input.
- Below480px the horizontal studio movement is disabled and its cards stack vertically.
- On narrow phones, links to `/projects/...` avoid Barba transitions and perform ordinary navigation.
- Some process text splitting is deliberately removed on mobile.

This is a valuable principle for Michael: the mobile composition should be re-authored, not merely shrunk.

### Performance and accessibility observations

The home hero is marked `loading="lazy"` in source, despite being the principal visual. That is a potential loading-priority weakness, not a field-measured performance failure. Michael’s hero should be eager with high fetch priority. Several other pages use responsive srcsets, but the case-study gallery replaces native source attributes through custom lazy-loading code. A simpler native `<picture>` and `loading="lazy"` strategy will be easier to maintain.

The featured-image behaviour listens for keyboard focus as well as hover. Testimonial arrows are assigned button roles, tabindex and Enter/Space handling. Reduced-motion detection is explicit in the testimonial component. This does not prove universal reduced-motion support across the entire site. The custom page transitions, preloader and long scroll tracks still need dedicated testing.

## SANTAL

### Positioning and visitor journey

SANTAL is a more conceptual presentation. It begins with a studio statement and progresses through philosophy, approach, work, services, process, company and contact on one long page. The navigation links are section anchors. A restrained grayscale system, extreme typographic scale, a visible grid and long scroll scenes create the impression of an architectural manifesto.

The inferred purpose is to demonstrate precision and confidence through the website’s own spatial behaviour. The page becomes a designed environment. Michael can learn from its disciplined framing, image isolation and scale contrast without adopting its full service range or its claims about engineering and procurement.

### Measured visual system

| Role | Source-observed value | Interpretation |
|---|---|---|
| Main dark | `#0f0f0f` | A deep neutral for immersive imagery and quiet contrast. |
| Main light | `#f0f0f0` | Pale text and fields with softer contrast than pure white. |
| Highlight line | `#f2f0f033` | An approximately20%-opacity structural rule. |
| Faint dark-background line | `#f2f0f00d` | An approximately5%-opacity rule, present but restrained. |
| Muted text | `#f2f0f066` and `#0f0f0f66` | Secondary typography is created through opacity rather than unrelated color. |
| Type | locally served Helvetica400/500, WOFF2, font-display swap | One type family establishes a systematic tone. |
| Root scaling | `font-size:calc(16 / var(--viewport-width) * 100vw)` | Many measurements scale as a coordinated composition. |
| Desktop reference width | 1440 | The source scales its rem-based scene against this width. |
| Mobile reference width | 416 | A separate composition reference replaces the desktop scale. |
| Main grid | 8equal columns, 1rem gap | Repeated half/quarter boundaries support the visual choreography. |
| Mobile grid | 4columns below1024px | A deliberate structural simplification. |
| Padding | 1rem outer, .5rem small | Tight controlled edges maintain architectural precision. |
| Display H1 | 14.625rem, 87% leading, -.1em tracking, uppercase | Very large, tightly packed type becomes a spatial object. |
| Offset scale | 2,4,6,8,12,16,32,72,128,172,256px equivalents at base | A coherent spacing ladder includes large scene-level gaps. |

The main breakpoint is1023/1024px, repeated across many component rules. Large offsets also shrink on mobile, for example16rem→10.75rem and8rem→5.5rem.

### Grid as identity

The hero includes persistent vertical lines at12.5% and62.5% of the viewport plus a diagonal line. These are not arbitrary decorations: they use eighth-column positions and tie typography, image reveals and navigation into a shared coordinate system. Half-viewport and quarter-viewport boundaries recur in the services section.

The header is sticky, occupies50lvh in its source composition and can use `mix-blend-mode:difference`. A compact interface and large logo treatment share the same system. Blend mode allows foreground marks to invert over changing light and dark visual fields. It needs testing over complex photography because contrast cannot be assumed from the CSS alone.

The mobile menu reduces inactive link opacity to .3. The active item becomes opaque and gains a thin vertical marker. This is a clear state grammar with very little decoration.

### Services choreography

The services section is an engineered scroll sequence. Its track height is `175lvh + itemCount × 100lvh`, giving each service a full viewport of scroll travel. A sticky100lvh viewport clips large labels and media. Titles and media occupy quarter-width units, and the media rail starts outside the visible frame. Clipped duplicate text layers create highlighted and subdued regions. A difference-blend layer contributes to the changing contrast.

Desktop descriptions sit in an absolutely positioned area near the mid-height of the scene, with a maximum width of20.5625rem. On mobile they become normally positioned, centred text with a22.75rem maximum. This is a composed transition between two modes, not a uniform scale reduction.

The inferred commercial purpose is to give each capability a distinct moment of attention. For a visualiser with a finite set of services, a shorter accessible set of rows can provide the same hierarchy with far less scrolling and processing cost.

### Work, process and company

The work section starts from a centrally clipped reveal (`clip-path:inset(0 50%)`). The visible gallery uses three columns on desktop and two on mobile, with much smaller mobile gaps. A load-more control limits the initially exposed visual inventory. Project items declare `will-change:transform,opacity`, indicating animated movement or entrance effects.

The process is an accordion layered into a long sticky scene. Its bodies begin at height0 with overflow hidden. Mobile headers become a two-column grid. The captured public copy repeats the same long description and scope beneath multiple stages. This is an editorial weakness to avoid: Michael’s project captions must each explain the image actually shown.

The company scene extends over several viewport heights, uses difference blending and keeps a description in the grid’s lower-right area. The footer then resolves into a practical contact hierarchy, with separate email types and a location. Michael needs a much simpler single enquiry address and no invented office, team or business-service claims.

### Technical stack and motion

The captured HTML is server-rendered Nuxt markup with hashed `_nuxt` bundles. Source inspection confirms Vue, GSAP3.15.0, Lenis, Swiper and Three.js classes in delivered JavaScript. The Three.js code and canvas elements show that at least some scenes use graphics rendering. The source alone does not establish that every visual is rendered through WebGL.

CSS defines `.3s`, `.5s` and `.8s` motion tokens using `cubic-bezier(.25,1,.5,1)`. Source uses GSAP scrubbing for scroll-dependent scenes. A text animation function uses1.6seconds, .03second stagger and .2second delay. One pointer-motion routine reads `prefers-reduced-motion` and disables its displacement on small screens or when reduced motion is requested. That local handling should not be mistaken for a verified whole-site reduced-motion policy.

There is a mobile landscape branch that hides the Nuxt scene and displays a rotate-phone graphic. For Michael’s portfolio this restriction should be avoided. Visitors should be able to view architecture in landscape, particularly drawings and wide renders.

### Performance implications

Captured uncompressed source sizes were approximately397KB for shared CSS,55KB for page CSS,413KB for the entry bundle and439KB for the page bundle. These are raw downloaded file sizes, not compressed network transfer measurements, and exclude images, fonts and other requests. They demonstrate the complexity of the implementation, not a measured load-time score.

SANTAL’s spectacle involves overlapping sticky layers, clipping, canvas, scroll smoothing and animation scheduling. Michael’s primary asset is the architectural imagery itself. Using local WOFF2 fonts, responsive AVIF, static HTML, modest CSS transforms and a small interaction script preserves that imagery while keeping work on the main thread low.

## Transferable decisions for Michael’s portfolio

| Source principle | Portfolio adaptation | Avoid |
|---|---|---|
| BCG gives the built work the first read | Start with one strong approved render and a clear personal signature. | Competing slides, badges or generic sales cards over the hero. |
| BCG’s editorial project evidence | A separate page per project with an overview, four renders, sketch and blueprint. | Uncaptioned image dumps or identical captions. |
| BCG re-authors mobile behaviour | Stack the editorial layouts naturally and make every action touch-accessible. | Hover-only project navigation. |
| SANTAL uses a shared coordinate system | Repeated fine rules, project numbering and aligned captions. | Decorative grid lines with no layout relationship. |
| SANTAL creates emphasis through scale contrast | Large restrained headings paired with small, readable project metadata. | Tiny body text or permanently oversized text crowding images. |
| Both use deliberate pacing | Short one-time reveals and calm transitions between distinct sections. | Blocking preloaders and mandatory scroll choreography. |
| Both make the next step obvious | Persistent project index and a clear email invitation at the end. | A contact form that cannot submit on static hosting. |

## Source register

### BCG primary pages

- https://www.bcgbuildingdesign.com.au/
- https://www.bcgbuildingdesign.com.au/studio
- https://www.bcgbuildingdesign.com.au/process
- https://www.bcgbuildingdesign.com.au/project
- https://www.bcgbuildingdesign.com.au/projects/the-kembali
- https://cdn.prod.website-files.com/6a794e5aeebba97e3ac774ae/css/bcg-staging.webflow.shared.4c5b110df.min.css

The root HTML includes the cited custom JavaScript inline. The footer credits uBloom Digital. Downloaded research copies are in `research/source/bcg-*`.

### SANTAL primary pages and assets

- https://santalarch.com/
- https://santalarch.com/#services
- https://santalarch.com/_nuxt/entry.D7X7o5bn.css
- https://santalarch.com/_nuxt/index.4_khxnMZ.css
- https://santalarch.com/_nuxt/DrgmgFce.js
- https://santalarch.com/_nuxt/tMB0Uc8w.js

The footer credits The First The Last. Hashed assets may change after future deployment. Downloaded research copies are in `research/source/santal-*`. Proprietary source files are for internal analysis and should be excluded from the public portfolio repository.
