# drCWDugan — BUSINESS CONTEXT (read FIRST, every session)

> **Purpose:** the single inventory of everything that already exists on the drCWDugan business side, so no asset is built blind or duplicated. **Load this at the start of ANY drCWDugan brand / website / marketing / asset session, before building anything.** If something here is stale, fix it here — this file is the map.
> Last refreshed: 2026-06-18.

## ⚠ J-1 WORK RIGHTS — SETTLED, DO NOT RE-LITIGATE
**Cory CAN be paid NOW.** RO Amy Gueho cleared it: earning **AUD from Australian clients via his ABN** (AUD into his AU bank) is completely fine while he is in the US on J-1 — it's only a routine item he raises with his accountant at AU tax-return time (he is not using any tax treaties). The mining/OH ICP is AU-based → squarely in the cleared lane, so paid work there is **real revenue now, not pipeline-for-later.** Only **US-based / USD clients** are out of scope. Free tools/demos/skill-building are always fine. The niche doc's "validation now = no paid work" line is OVER-conservative — this clearance supersedes it. (memory `feedback_j1_paid_consulting_settled`)

---

## 1. THE LIVE WEBSITE (it already exists — don't rebuild from zero)
- **Live URL:** https://drcorydugan.com (custom domain). **Registrar = Squarespace Domains** (registered 2026-03-25, renews 2027-03-25; RDAP-verified 2026-07-05); **DNS = Google Cloud DNS via Squarespace** (account.squarespace.com → Domains → DNS) — NOT Netlify DNS (Netlify has no zone for it; it only serves the site via the A/CNAME records). Email: ⚠ NO MX records exist on the domain (dig-verified 2026-07-17), so the "contact@ forwards via ImprovMX" setup is NOT active. Do NOT use or publish contact@drcorydugan.com anywhere until MX is actually configured. Public contact = cory.dugan1@gmail.com. SPF is "v=spf1 -all", so nothing can send AS the domain; any transactional or report email must send via Gmail or Apps Script until MX + SPF/DKIM are added (in the Cloudflare zone after migration). The old "registered via Netlify 2026-06-13" note was wrong.
- **Codebase:** `~/Documents/GitHub/drcwd-website/` → `github.com/corydugan/drcwd-website`. Plain static HTML (no framework): `index.html`, `clients.html` (How It Works), `evidence.html`, `publications.html`, `iron-protocol.html`, `for-individuals.html` (coaching page), two article pages, `thank-you.html`, `images/`, `downloads/`, `_redirects`, `sitemap.xml`. (Rebuilt on v3, homepage + interior, 2026-06-20.)
- **Deploy:** Netlify (Cory's team), site `drcorydugan` id `41e94978-8512-456f-b29e-f955f935d64d`. ⚠ **MANUAL deploy from the `drcwd-website` REPO via `netlify deploy --prod` — NOT git-CI, and NOT from the old `netlify-deploy/` folder.** Re-verified via Netlify 2026-07-02 (live deploy = `deploy_source: api`; no `netlify.toml`/GitHub workflow; a `git push` does NOT ship the site — the CLI just stamps the working-dir commit ref onto the upload). Do NOT assume committing/pushing ships live — you must run `netlify deploy --prod`. Full detail in §6 item 2.
- **Current site structure (top→bottom):** header+nav · hero · headshot · credentials bar · About (Researcher/Educator/Athlete) · The Journey · client testimonials · Services (3) · credentials deep-dive · In Action gallery · podcast · data-dashboard mockup · Pricing · FAQ · Free Resources · Discovery-Call CTA · footer.
- **Nav:** About · Services · Pricing · FAQ · The Iron Protocol · Evidence · Resources · Book a Call.

## 2. POSITIONING & OFFERS (what the business actually sells)
**The live site is COACHING-FORWARD; the current pivot is HEALTH-SCREENING-AI-FORWARD. These don't fully match yet — see §6.**
- **Coaching (individuals):** professional women (FIFO, mining, corporate, healthcare, academia) — burnout, energy/fatigue, iron deficiency. Tiers: **Kickstart $120 one-time** (2 sessions) · **Holistic $199/mo** (most popular, 3-mo min) · free **Iron Protocol** download.
- **Consulting (organisations):** program design, evidence reviews, women's-health initiatives — wellness cos, health-tech, HR. "Quoted per project."
- **Research & data analysis:** biostatistics, health-data pipelines, study design — research groups, pharma/biotech.
- **Health-Screening AI consulting (the pivot):** canonical niche + ICP at `DR.CWD/strategy/06082026 Niche + ICP CANONICAL_CD.md` (moved 2026-06-25 in the DR.CWD consolidation; the whole business is now indexed by `DR.CWD/drCWDugan ENGINE.md`); **IRON RISK CHECK** demo LIVE at https://iron-risk-check.netlify.app is the flagship product/proof. ⚠ NAMING: the old name "IRON-5" was RETIRED 2026-07-14 because it collides with another group's published, validated instrument (Vinge et al., PMID 41916414); Cory's tool is NOT derived from it (17 items vs 5, binary tier vs threshold). Never re-introduce "IRON-5" as the product name; citing the Vinge instrument by its name is fine. This is the direction the v3 "Authority" brand was built for.
- **Proof points used:** 10+ yrs research · PhD UWA · 30+ publications · featured ABC Radio / BJSM / JAMA Network Open / Healio / MedPage. **⚠ Numbers defer to `DR.CWD/CANONICAL FACTS — drCWDugan (single source of truth)_CD.md` — verify there before quoting (screening reach = 3,000 women, NOT 10,000; pubs = 30+, NOT 25+). "$850K+ funding" and "34,000 members" were REMOVED 2026-07-02 — do NOT reintroduce.**

## 3. BRAND SYSTEM (how everything should look)
- **Canonical:** `~/Documents/GitHub/drcwd-design-system/` (this repo) = v3 "Authority". Grape `#352051` + DM Serif Display/DM Sans, white-dominant editorial, evidence/stat motif, Δ delta logo. Live visual home: claude.ai/design id `27287049-8ee5-4962-95f4-24d9cde8f6de`.
- Full spec: this repo's `README.md`. Paste-context: `SKILL.md`.

## 4. STOREFRONT / MONEY / DOMAIN
- **Payments:** Stripe (payment links wired into the site's Pricing CTAs).
- **Domain:** drcorydugan.com (owned). **Booking:** Cory's Google appointment-schedule link (NOT Calendly, despite Calendly existing).
- **Business docs** (`DR.CWD/infra/business-docs/`): Business Plan (2026-03-24), ABN registration, Iron Protocol ebook PDF, domain receipt.
- **ABN:** registered (AU) — relevant to J-1 work-rights rules (AU-payers OK; US/USD clients out of scope).

## 5. SOCIAL & DISTRIBUTION
- **LinkedIn** in/cory-dugan-phd (optimised 2026-06-18, "Founder & Health-Screening AI Consultant") · **IG** @dr.cwdugan · **FB** /dr.cwdugan · **X** @CoryDugan10 · GitHub portfolio.
- **Buffer** connected (distribution rail for social content). **Social Media Procedure Manual** + build-out plan in `DR.CWD/`.
- *(HolisticHer @_holisticher is a SEPARATE brand, winding down → CWD absorbing the niche. Different design system: gradient + Montserrat. Never mix.)*

## 6. ⚠ KNOWN DRIFTS / RECONCILE BEFORE BUILDING
*(renumbered + de-duplicated 2026-06-30 — was 1/3b/4/2/3 with two positioning + two deploy entries.)*

1. **[RESOLVED 2026-07-05, re-verified 2026-07-17] Interior-page color rebrand is DONE.** Phase B rebranded every interior page to grape v3; a grep on 2026-07-17 found ZERO navy `#171b2e` / indigo `#6366f1` / teal in the tree, and for-individuals / iron-protocol / clients / publications all carry grape `#352051`. No color-token swap remains (logo + favicon/OG asset polish may still be open; tracked in JSON northstar_s18 ebook cover). ⚠ NOTE: a full clean-slate rebuild on Cloudflare Pages is now planned (spec: `DOWNLOADS 📥/07172026 drcorydugan.com Rebuild — BUILD SPEC (Fable)_CD.md`), which supersedes the "don't rebuild from zero" framing in §1 for that deliberate, salvage-manifest-seeded rebuild.

2. **Deploy source — RESOLVED 2026-06-30 (was an open question).** The live site (Netlify project `drcorydugan`, site id `41e94978-8512-456f-b29e-f955f935d64d`, team `69c469c724a4a9e8701de426`) is currently serving deploy **`6a34666`** (created 2026-06-18, `deploy_source: api`, commit_ref `1fe371c` from the **`drcwd-website` repo**). So the live content IS the repo's, deployed **manually/API — NOT continuous Netlify→GitHub CI.** The old `DR.CWD/netlify-deploy/` folder is **stale** (its `<title>` no longer matches live) and can now be RETIRED — a fresh manual deploy FROM THE REPO was confirmed live 2026-07-02 (`deploy_source: api`, carrying repo commit `752564c`). ✅ **The `10,000+` deploy-lag is RESOLVED** (was commit `935212a` undeployed) — live homepage verified 2026-07-02 serving `3,000+` women, `30+` pubs, and NO `10,000+` / `$850K+` / `34,000+` / Lancet. Repo is now at `632bd77`, fully shipped + pushed. END STATE (Phase 2, optional): wire Netlify→GitHub continuous deploy so the repo is the single source and the manual folder retires (needs an interactive GitHub OAuth in the Netlify dashboard).

3. **Positioning mismatch (strategic).** Live site leads with **COACHING to individual women** ($120 Kickstart / $199-mo Holistic), while the canonical strategy + v3 brand + LinkedIn lead with **healthcare-AI authority: health-screening TOOLS for MINING/occupational-health orgs** (IRON RISK CHECK; LOCKED tiered pricing per CANONICAL FACTS 2026-06-25: **low founding-design-partner PILOT / $15-25k STANDARD build / $25-40k PREMIUM**, three tiers, product-not-retainer; the old $8-15k is superseded). A rebrand must decide how hard to swing the public site toward the AI/consulting offer vs keep coaching as a secondary lane.

## 7. DISAMBIGUATION — "when Cory says X, here's what already exists"
| Cory says… | Reality | Likely intent |
|---|---|---|
| "build a landing page" | a full multi-page site already exists at drcorydugan.com | (a) rebrand existing site to v3, (b) ADD a focused landing page (e.g. IRON RISK CHECK / consulting) to it, or (c) a standalone campaign page — **ask which** |
| "the website" | `drcwd-website` repo → Netlify → drcorydugan.com | edit the existing repo, not a new build |
| "update pricing / services" | edit `index.html` Pricing/Services sections | in-place edit + redeploy |
| "a new tool / questionnaire" | research-tool-builder skill; sold via Stripe | net-new product |
