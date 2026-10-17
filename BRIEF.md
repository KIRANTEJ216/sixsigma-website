# BRIEF — Six Sigma Solutions

> **Status note (added at delivery).** The working title above was "Brand Signages",
> a generic placeholder used while the build was unnamed. It is now **Six Sigma
> Solutions**, outdoor sign board manufacture, fabrication and installation, on
> **+91 96423 86767**. Section 08 was also reframed: it reads "Typical
> environments" rather than "Selected work", because no photographed building on
> the page is a confirmed Six Sigma job. Adding real case studies flips the
> section back automatically — see `REAL_PROJECTS` in `index.html`.
>
> **Colour theme.** Two complete palettes ship. A cool light ground (`#EDF1F7`
> canvas, white surfaces, dark ink) and a dark one (`#04050A` canvas, near-black
> surfaces, light ink). The visitor toggle sits in the top bar, the choice is
> stored in `localStorage["ss-theme"]`, and it falls back to the operating-system
> preference. An inline script in `<head>` resolves the theme before first paint,
> so there is no flash. Both themes were contrast-checked at desktop and mobile,
> and the layout was audited for horizontal overflow from 320 px upward.
>
> Photographs are night scenes and are intentionally kept as dark plates in the
> light theme rather than being recoloured — they are the warm/cool thesis.

**Self-authored under explicit creative delegation.**
The user supplied a complete, highly detailed creative brief and asked for it to be
built ("create a website with this prompt using scrollcraft skills"). Every answer
below is either lifted verbatim from that brief or a clearly-labelled authored
decision made inside the scope they specified. No answers were invented to fill gaps.

---

## 1. Vibe (3–5 words) + references

**Verbatim from the brief:**

> "The page should feel closer to a premium architecture, automotive, or technology
> website than a conventional printing-service website."

> "Make the website feel engineered, precise, durable, and premium."

Five words: **engineered, precise, durable, architectural, night-lit.**

Reference register the brief names: architecture studio sites, automotive, technology.
It explicitly rejects the "generic white business template" and the printing-service
genre. It asks for "slow, deliberate, architectural — not excessive bouncing or spinning."

---

## 2. Scroll journey, section by section

**Verbatim section list from the brief, in the order given:**

1. Hero — building transforms into illuminated signage
2. Brand value — large typography fades and moves with scroll; "Be Seen. Be Remembered. Be Chosen."
3. Visibility problem — before/after split, poor visibility → strong visibility
4. Signage categories — "Each sign type builds onto a façade"
5. Materials — exploded view, layers separate
6. Process — consultation to installation timeline
7. Portfolio — horizontal case-study gallery
8. Customisation — user chooses material, lighting, style
9. Proof — metrics and testimonials reveal progressively
10. Quote form — building remains in background
11. FAQ — clean accordion

The brief also specifies the hero scroll script in exact percentages (0–15% empty
building at dusk, 15–30% measurement grid, 30–45% wireframe, 45–60% layer assembly,
60–75% lighting on, 75–90% completed illuminated building, 90–100% quote CTA).

**Journey beats (authored, serving the brief's section list):**

```
1  Recognition   their own blank building, at dusk
2  Tension       the cost of being invisible, named plainly
3  Turn          the building assembles and ignites
4  Substance     what it is made of, in layers they can read
5  Range         what they can choose from
6  Commitment    one action, pre-filled with their own selections
```

---

## 3. Energy curve

**Verbatim from the brief:**

> "Motion: slow, deliberate, architectural—not excessive bouncing or spinning."

> "Use cinematic motion for the hero and product storytelling, then use calmer layouts
> for trust, project details [etc]."

Loud at exactly one place (the hero transformation), calm everywhere else. Nothing
punchy, nothing fast. Administrative content (proof, FAQ, form) is compressed to flow
sections rather than given scroll room.

---

## 4. Feeling curve and the peak

Written **before** the acts existed, per feel.md §1.

```
Plate   Emotion        Caused by
─────   ───────        ─────────
1a      Recognition    their own building at dusk, held still, no signage, blue hour
1b      Curiosity      a measurement grid wakes up and begins scanning the facade
1c      Awe      ★     the sign assembles out of nothing and the LEDs ignite at night
2       Unease         a plain building rendered flat and grey on a wide street
3       Conviction     "Be Seen. Be Remembered. Be Chosen." landing one at a time
4       Appetite       eight signage solutions travelling sideways, each landing whole
5       Confidence     an exploded signboard held still and labelled like a real drawing
6       Reassurance    five steps from consultation to install, arriving in sequence
7       Agency         their own selections rewriting the preview as they choose
8       Proof          completed work travelling laterally, each card fact-labelled
9       Resolve        a specification half-written for them, one action
```

**Adjacent-feeling check:** 1b→1c are deliberately different (curiosity then awe, awe
being the payoff). 1c→2 is awe into unease, a hard drop, which is what makes the
hero's ending land. No two adjacent plates carry the same feeling. No filler.

### The peak

**Plate 1c**, the last third of the hero.

> *"I scrolled and the blank building I was looking at grew its own sign and turned it on."*

It gets the largest span on the page, the silence in front of it (plate 1b is quiet:
only the grid moves, no copy assembles), and the entire drawing budget. Plate 2, the
next one down, is deliberately flat and grey — the loudest thing on the page needs a
quiet thing immediately after it or it has nothing to have been loud against.

### The tell-someone sentence

> **It's the site where a blank building grows its own sign as you scroll, and by the
> time you reach the quote form it's already written half the specification for you.**

The signature move lives inside this sentence. The peak and the signature move point
at the same mechanism — the document filling itself in as you read it.

---

## 5. One thing this site should do that no site they have seen does

**Verbatim intent from the brief** (this section is the seed):

> "Customisation studio: create a visual interactive selector... As the user changes
> selections, update the preview panel."

> "Lead-generation section: Form fields: ... Required signage, Approximate dimensions"

The brief asks for a customiser *and* a quote form that collects specifications. Those
are usually two disconnected things: a fun toy, then a blank form the visitor fills
from scratch.

### The signature move — **The running Bill of Materials**

A fixed margin panel, typeset as a printed estimate sheet with a torn top edge and a
dotted tear rule down its side, present for the whole page.

- Every plate the visitor scrolls past **stamps a real catalogue line into it**:
  `ACP facade panel · 4 mm · graphite`, `3D LED letter · 350 mm face · halo lit`,
  `Aluminium mounting rail · 60 × 40 mm`.
- The **customisation studio writes into it directly** as selections are made.
- The **quote form is pre-filled from it**: the "Required signage" and "Approximate
  dimensions" fields arrive already populated, because the visitor spent the page
  building them.

Every line is a real product the company sells with real, checkable specification. No
invented prices, no invented totals, no fake metrics. It is a genuine quotation being
compiled by the visitor, which is also the qualification the sales team actually wants.

Why this passes the test: describe it to someone who has seen a hundred agency sites
and they cannot place it. A page that hands you a filled-in specification at the form
is not a device, it is a different kind of page.

---

## 6. How far from premium-minimal

**Verbatim from the brief:**

> "Cards: minimal glass panels with subtle borders."
> "Use subtle grid lines, measurement marks, blueprint overlays, and technical labels."
> "Avoid generic stock images, excessive gradients, cartoon illustrations, and crowded layouts."

Range chosen: **dense-technical within a premium-minimal shell.** A restrained ground
(in either palette — see the colour-theme note above), one accent, generous air, but
the *content* is information-forward — spec tables, tolerances, dimension lines,
line-item ledgers, technical annotations. The brief asks for both, so both are
honoured: minimal chrome, dense information.

**Palette rotation note (taste.md).** Off-black with warm amber is on the rotation list,
and here it is *earned* rather than reached for: this page is literally about light being
installed on a building. The amber is the LED. The cool near-white is the blueprint ink.
The warm/cool split is the visual thesis. Avoiding the banned cream-and-brass artisan
palette entirely. The light theme keeps the same amber accent against a cool pale
ground, so the amber still reads as *installed light* rather than as a brand colour.

---

## 7. One unbroken world, or distinct scenes?

**Authored decision: distinct plates.** Explicitly not one continuous world.

The brief asks for a strong scroll-driven hero and then eleven distinct, individually
scannable business sections (categories, portfolio, FAQ, quote form). A continuous
worldflight forbids section boundaries, which would delete most of what the brief is for.
The hero is cinematic and continuous; everything after it is a plate. This is the brief's
own instruction: "The ideal experience is not animation everywhere. Use cinematic motion
for the hero and product storytelling, then use calmer layouts for trust, project details."

---

## 8. Assets

**User answered (Step 0 question 8):** to paste a `KIE_AI_API_KEY` for generated
imagery, and to supply real business contact details.

Not yet supplied at time of writing. See "Asset deviation" below.

### Asset deviation, recorded

**The hero is a drawn SVG assembly, not a generated image sequence.** This is an
authored decision and it overrides the brief's "use a scroll-scrubbed image sequence with
approximately 60–120 optimized frames" recommendation.

Reason: an AI video model cannot hold a building perfectly static while signage
assembles onto it. Across 60–120 frames the façade drifts, warps and deforms, which is
visually fatal for a transformation whose entire value is that the *building does not
move*. The drawing also satisfies the brief's own design language more directly
("measurement marks, blueprint overlays, technical labels"), pauses and reverses exactly,
weighs roughly 30 KB against several megabytes, and holds Core Web Vitals.

Generated photography is still used where real imagery carries information the drawing
cannot: material close-ups and portfolio plates. That needs the key.

---

## Verification notes for the Step 5 pass

- **Authored silence:** none. There is no empty viewport before the peak. Plate 1b
  (the quiet grid scan) is a *pinned act with content already present*, not an empty
  screen. Do not classify it as dead scroll.
- **Placeholder content is expected.** Portfolio entries, testimonials and metrics are
  deliberately marked placeholders pending real data from the user. The harness will
  report zero `count` devices by design, because invented statistics are banned.