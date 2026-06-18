# drCWDugan — BUSINESS CONTEXT (read FIRST, every session)

> **Purpose:** the single inventory of everything that already exists on the drCWDugan business side, so no asset is built blind or duplicated. **Load this at the start of ANY drCWDugan brand / website / marketing / asset session, before building anything.** If something here is stale, fix it here — this file is the map.
> Last refreshed: 2026-06-18.

---

## 1. THE LIVE WEBSITE (it already exists — don't rebuild from zero)
- **Live URL:** https://drcorydugan.com (custom domain, registered 2026-06-13; receipt in `business-docs/`).
- **Codebase:** `~/Documents/GitHub/drcwd-website/` → `github.com/corydugan/drcwd-website`. Plain static HTML (no framework): `index.html`, `clients.html` (How It Works), `evidence.html`, `publications.html`, `iron-protocol.html`, two article pages, `thank-you.html`, `images/`, `downloads/`, `_redirects`, `sitemap.xml`.
- **Deploy:** Netlify (Cory's team). The GitHub repo is the source. ⚠ There is ALSO a `DR.CWD/netlify-deploy/` Drive folder with an older partial copy of the site — treat the **GitHub repo as canonical**; confirm before ever deploying from the Drive folder.
- **Current site structure (top→bottom):** header+nav · hero · headshot · credentials bar · About (Researcher/Educator/Athlete) · The Journey · client testimonials · Services (3) · credentials deep-dive · In Action gallery · podcast · data-dashboard mockup · Pricing · FAQ · Free Resources · Discovery-Call CTA · footer.
- **Nav:** About · Services · Pricing · FAQ · The Iron Protocol · Evidence · Resources · Book a Call.

## 2. POSITIONING & OFFERS (what the business actually sells)
**The live site is COACHING-FORWARD; the current pivot is HEALTH-SCREENING-AI-FORWARD. These don't fully match yet — see §6.**
- **Coaching (individuals):** professional women (FIFO, mining, corporate, healthcare, academia) — burnout, energy/fatigue, iron deficiency. Tiers: **Kickstart $120 one-time** (2 sessions) · **Holistic $199/mo** (most popular, 3-mo min) · free **Iron Protocol** download.
- **Consulting (organisations):** program design, evidence reviews, women's-health initiatives — wellness cos, health-tech, HR. "Quoted per project."
- **Research & data analysis:** biostatistics, health-data pipelines, study design — research groups, pharma/biotech.
- **Health-Screening AI consulting (the pivot):** canonical niche + ICP at `DR.CWD/Health-Screening Consulting/06082026 Niche + ICP CANONICAL_CD.md`; **IRON-5** demo (live, on LinkedIn) is the flagship product/proof. This is the direction the v3 "Authority" brand was built for.
- **Proof points used:** 10+ yrs research · PhD UWA · 25+ publications · $850K+ funding · featured ABC Radio / BJSM / JAMA Network Open / Healio / MedPage.

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
1. **Live site is OFF-BRAND (verified 2026-06-18).** `drcwd-website` (last commit 2026-05-30) uses an **indigo/violet `#6366f1` + pink palette on DARK backgrounds** — NOT grape, NOT teal (verified: 15 indigo hits, 0 grape across 6 pages). It does use DM Serif Display + DM Sans. So the public site matches neither v2 grape nor v3 "Authority"; it's white-dominant-editorial's opposite (dark + colorful). Any site work = a full rebrand-to-v3 (color + light/editorial feel + delta logo + stat motif), not a tweak.
2. **Positioning mismatch.** Live site leads with coaching; the pivot + v3 brand + LinkedIn lead with healthcare-AI authority. Decide how hard to swing the site toward the AI/consulting offer.
3. **Duplicate deploy folder.** `DR.CWD/netlify-deploy/` vs the GitHub repo — confirm the repo is the only deploy source; the Drive copy is stale.

## 7. DISAMBIGUATION — "when Cory says X, here's what already exists"
| Cory says… | Reality | Likely intent |
|---|---|---|
| "build a landing page" | a full multi-page site already exists at drcorydugan.com | (a) rebrand existing site to v3, (b) ADD a focused landing page (e.g. IRON-5 / consulting) to it, or (c) a standalone campaign page — **ask which** |
| "the website" | `drcwd-website` repo → Netlify → drcorydugan.com | edit the existing repo, not a new build |
| "update pricing / services" | edit `index.html` Pricing/Services sections | in-place edit + redeploy |
| "a new tool / questionnaire" | research-tool-builder skill; sold via Stripe | net-new product |
