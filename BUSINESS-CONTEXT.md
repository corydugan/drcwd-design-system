# drCWDugan — BUSINESS CONTEXT (read FIRST, every session)

> **Purpose:** the single inventory of everything that already exists on the drCWDugan business side, so no asset is built blind or duplicated. **Load this at the start of ANY drCWDugan brand / website / marketing / asset session, before building anything.** If something here is stale, fix it here — this file is the map.
> Last refreshed: 2026-06-18.

## ⚠ J-1 WORK RIGHTS — SETTLED, DO NOT RE-LITIGATE
**Cory CAN be paid NOW.** RO Amy Gueho cleared it: earning **AUD from Australian clients via his ABN** (AUD into his AU bank) is completely fine while he is in the US on J-1 — it's only a routine item he raises with his accountant at AU tax-return time (he is not using any tax treaties). The mining/OH ICP is AU-based → squarely in the cleared lane, so paid work there is **real revenue now, not pipeline-for-later.** Only **US-based / USD clients** are out of scope. Free tools/demos/skill-building are always fine. The niche doc's "validation now = no paid work" line is OVER-conservative — this clearance supersedes it. (memory `feedback_j1_paid_consulting_settled`)

---

## 1. THE LIVE WEBSITE (it already exists — don't rebuild from zero)
- **Live URL:** https://drcorydugan.com (custom domain, registered 2026-06-13; receipt in `business-docs/`).
- **Codebase:** `~/Documents/GitHub/drcwd-website/` → `github.com/corydugan/drcwd-website`. Plain static HTML (no framework): `index.html`, `clients.html` (How It Works), `evidence.html`, `publications.html`, `iron-protocol.html`, `for-individuals.html` (coaching page), two article pages, `thank-you.html`, `images/`, `downloads/`, `_redirects`, `sitemap.xml`. (Rebuilt on v3, homepage + interior, 2026-06-20.)
- **Deploy:** Netlify (Cory's team). ⚠ **The live deploy source is currently the manual `DR.CWD/netlify-deploy/` upload, NOT auto-deploy from the GitHub repo — see §6.3b** for the verified detail + one open question. Do NOT assume editing the repo ships live until §3b is reconfirmed.
- **Current site structure (top→bottom):** header+nav · hero · headshot · credentials bar · About (Researcher/Educator/Athlete) · The Journey · client testimonials · Services (3) · credentials deep-dive · In Action gallery · podcast · data-dashboard mockup · Pricing · FAQ · Free Resources · Discovery-Call CTA · footer.
- **Nav:** About · Services · Pricing · FAQ · The Iron Protocol · Evidence · Resources · Book a Call.

## 2. POSITIONING & OFFERS (what the business actually sells)
**The live site is COACHING-FORWARD; the current pivot is HEALTH-SCREENING-AI-FORWARD. These don't fully match yet — see §6.**
- **Coaching (individuals):** professional women (FIFO, mining, corporate, healthcare, academia) — burnout, energy/fatigue, iron deficiency. Tiers: **Kickstart $120 one-time** (2 sessions) · **Holistic $199/mo** (most popular, 3-mo min) · free **Iron Protocol** download.
- **Consulting (organisations):** program design, evidence reviews, women's-health initiatives — wellness cos, health-tech, HR. "Quoted per project."
- **Research & data analysis:** biostatistics, health-data pipelines, study design — research groups, pharma/biotech.
- **Health-Screening AI consulting (the pivot):** canonical niche + ICP at `DR.CWD/Health-Screening Consulting/06082026 Niche + ICP CANONICAL_CD.md`; **IRON-5** demo (live, on LinkedIn) is the flagship product/proof. This is the direction the v3 "Authority" brand was built for.
- **Proof points used:** 10+ yrs research · PhD UWA · 30+ publications · $850K+ funding · featured ABC Radio / BJSM / JAMA Network Open / Healio / MedPage. **⚠ Numbers defer to `DR.CWD/CANONICAL FACTS — drCWDugan (single source of truth)_CD.md` — verify there before quoting (screening reach = 3,000 women, NOT 10,000; pubs = 30+, NOT 25+).**

## 3. BRAND SYSTEM (how everything should look)
- **Canonical:** `~/Documents/GitHub/drcwd-design-system/` (this repo) = v3 "Authority". Grape `#352051` + DM Serif Display/DM Sans, white-dominant editorial, evidence/stat motif, Δ delta logo. Live visual home: claude.ai/design id `27287049-8ee5-4962-95f4-24d9cde8f6de`.
- Full spec: this repo's `README.md`. Paste-context: `SKILL.md`.

## 4. STOREFRONT / MONEY / DOMAIN
- **Payments:** Stripe (payment links wired into the site's Pricing CTAs).
- **Domain:** drcorydugan.com (owned). **Booking:** Cory's Google appointment-schedule link (NOT Calendly, despite Calendly existing).
- **Business docs** (`DR.CWD/business-docs/`): Business Plan (2026-03-24), ABN registration, Iron Protocol ebook PDF, domain receipt.
- **ABN:** registered (AU) — relevant to J-1 work-rights rules (AU-payers OK; US/USD clients out of scope).

## 5. SOCIAL & DISTRIBUTION
- **LinkedIn** in/cory-dugan-phd (optimised 2026-06-18, "Founder & Health-Screening AI Consultant") · **IG** @dr.cwdugan · **FB** /dr.cwdugan · **X** @CoryDugan10 · GitHub portfolio.
- **Buffer** connected (distribution rail for social content). **Social Media Procedure Manual** + build-out plan in `DR.CWD/`.
- *(HolisticHer @_holisticher is a SEPARATE brand, winding down → CWD absorbing the niche. Different design system: gradient + Montserrat. Never mix.)*

## 6. ⚠ KNOWN DRIFTS / RECONCILE BEFORE BUILDING
1. **Live site is OFF-BRAND on color, but closer than feared (verified 2026-06-18).** `drcwd-website` is **white-dominant editorial with DM Serif/DM Sans** (the feel + type are RIGHT) — but its accent palette is **navy `#171b2e` + indigo/violet `#6366f1`**, NOT grape `#352051` (0 grape hits across pages). So the rebrand is mostly a **color-token swap + logo + favicon/OG assets**, not a structure/feel rebuild. The teal→purple/indigo retheme was started in `DR.CWD/_website-work/` (color-option PNGs + `_pre-teal-backup/`) — that's why the site reads purple-ish; it never reached grape.
3b. **DEPLOY SOURCE — verified 2026-06-18, ONE OPEN QUESTION as of 2026-06-20.** The live site (Netlify project `drcorydugan`, site id `41e94978-8512-456f-b29e-f955f935d64d`, team `69c469c724a4a9e8701de426`) was **manually uploaded** (deploy_source "api", "triggered by upload") from `DR.CWD/netlify-deploy/` on 2026-06-12. As of that check it was **NOT connected to the GitHub repo** (`drcwd-website` — since rebuilt on v3 2026-06-20, now 9 files incl. for-individuals/clients/publications). **⚠ OPEN QUESTION (2026-06-20):** a later Netlify deploy (6a34666, 2026-06-18) carried a commit_ref into `drcwd-website`, which MAY mean the repo is now connected after all (the north-star reconcile project asserts "repo IS connected/live; netlify-deploy/ is now stale"). This is unconfirmed and the deploy is currently blocked on Netlify billing. **RE-VERIFY in Netlify at the next deploy (when billing clears), then rewrite this section to the single confirmed truth.** Until reconfirmed, treat `netlify-deploy/` as the live source and do not archive it. END STATE (Phase 2): one source = repo, Netlify→GitHub continuous deploy, manual folder retired.
4. **Positioning mismatch (strategic).** Live site sells **COACHING to individual women** ($120 Kickstart / $199-mo Holistic). The canonical strategy (`Health-Screening Consulting/Niche+ICP CANONICAL`) is **health-screening TOOLS for MINING/occupational-health orgs** (IRON-5, $8–15k builds, product-not-retainer). The public face and the strategic direction point in different directions — a rebrand should decide which the site leads with.
2. **Positioning mismatch.** Live site leads with coaching; the pivot + v3 brand + LinkedIn lead with healthcare-AI authority. Decide how hard to swing the site toward the AI/consulting offer.
3. **Duplicate deploy folder.** `DR.CWD/netlify-deploy/` vs the GitHub repo — confirm the repo is the only deploy source; the Drive copy is stale.

## 7. DISAMBIGUATION — "when Cory says X, here's what already exists"
| Cory says… | Reality | Likely intent |
|---|---|---|
| "build a landing page" | a full multi-page site already exists at drcorydugan.com | (a) rebrand existing site to v3, (b) ADD a focused landing page (e.g. IRON-5 / consulting) to it, or (c) a standalone campaign page — **ask which** |
| "the website" | `drcwd-website` repo → Netlify → drcorydugan.com | edit the existing repo, not a new build |
| "update pricing / services" | edit `index.html` Pricing/Services sections | in-place edit + redeploy |
| "a new tool / questionnaire" | research-tool-builder skill; sold via Stripe | net-new product |
