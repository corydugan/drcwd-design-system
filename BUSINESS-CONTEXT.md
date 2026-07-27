# drCWDugan BUSINESS CONTEXT (read FIRST, every session)

> **Purpose:** the single inventory of everything that already exists on the drCWDugan business side, so no asset is built blind or duplicated. **Load this at the start of ANY drCWDugan brand / website / marketing / asset session, before building anything.** If something here is stale, fix it here. This file is the map.
> **Last refreshed: 2026-07-27.** The previous refresh (2026-06-18) had drifted on four load-bearing facts about hosting, DNS and email. All four are corrected in §1 against live DNS.

---

## 0. THE ORGANISING MODEL (added 2026-07-27)

The business is **one capability, sold three ways, found through three layers**. Full working in `drCWDugan THREE-LAYER ARCHITECTURE.md`.

**The capability:** turning research and health data into decisions people can act on.

```
PACKAGES (what is sold)
  A. DONE FOR YOU ....... biostatistics, meta-analysis, SAPs, R pipelines
                          buyer: research groups, biotech, CROs, HEOR
                          5/5 skill · warm buyers · closes in DAYS
                          ⭐ THIS LEADS. Almost no regulatory load. See §8.
  B. DONE WITH YOU ...... screening design, workplace programs, governance
                          buyer: occ-health, mining/FIFO, women's health orgs
                          2/5 domain skill · 3-6 month procurement
                          ⛔ cannot sign until PI insurance is BOUND
  C. DONE BY YOU ........ tools, questionnaires, script packs, guides
                          buyer: individuals, researchers, orgs buying seats
                          build 5/5 · DISTRIBUTION 1/5 (the real constraint)
                          ⚠ the only package that generates US/USD leads
                            that cannot be legally converted before November

LAYERS (how buyers find him)
  1. CREDENTIAL ......... drcorydugan.com. Serves A and B.
                          ⭐ THE PERSONAL NAME IS CORRECT HERE, and a
                            descriptive brand would weaken it. B2B health
                            buyers buy a named expert with a PhD.
  2. ACQUISITION ........ a descriptive domain, IF ever built. Serves C only.
                          Sequenced LAST. Not a live decision.
  3. PRODUCT ............ Iron Risk Check, R Script Pack, Wheel of Life.
                          Already correct. Independent of the domain question.
```

**Consequence for naming:** a rebrand is a Layer 2 decision, Layer 2 serves the lowest-ticket package, and that package is sequenced last. It is not urgent. §9 lists the names that are already closed.

---

## ⚠ J-1 WORK RIGHTS: SETTLED, DO NOT RE-LITIGATE

**Cory CAN be paid NOW.** RO Amy Gueho cleared it: earning **AUD from Australian clients via his ABN** (AUD into his AU bank) is completely fine while he is in the US on J-1. It is only a routine item he raises with his accountant at AU tax-return time (he is not using any tax treaties). The AU-based ICP sits squarely in the cleared lane, so paid work there is **real revenue now, not pipeline-for-later.** Only **US-based / USD clients** are out of scope. Free tools, demos and skill-building are always fine. (memory `feedback_j1_paid_consulting_settled`)

---

## 1. THE LIVE WEBSITE (rebuilt 19 Jul 2026, now on Cloudflare)

- **Live URL:** https://drcorydugan.com
- **Host: CLOUDFLARE PAGES.** Migrated off Netlify 2026-07-19. Verified live 2026-07-27 (`server: cloudflare`, HTTP 200).
- **DNS: CLOUDFLARE.** Nameservers `sandy.ns.cloudflare.com` / `zahir.ns.cloudflare.com` (moved at Squarespace, 19 Jul). Registrar remains **Squarespace Domains** (registered 2026-03-25, renews 2027-03-25).
- **✅ EMAIL IS LIVE.** `cory@drcorydugan.com` **receives**, via Cloudflare Email Routing, forwarding to Gmail. Verified 2026-07-27: MX = `route1/2/3.mx.cloudflare.net`, SPF = `v=spf1 include:_spf.mx.cloudflare.net ~all`. DKIM added. The old `-all` SPF is gone.
  - 🔴 **SEND-AS IS NOT DONE.** He receives at cory@ but cannot yet reply *as* cory@. Open since 19 Jul, roughly a 10 minute job.
  - ⛔ `contact@drcorydugan.com` never existed and still does not. Use `cory@drcorydugan.com` or `cory.dugan1@gmail.com`.
- **Codebase:** `~/Documents/GitHub/drcwd-website/` → `github.com/corydugan/drcwd-website`. Plain static HTML, no framework.
  - **Branch: `rebuild-cloudflare`** (NOT `main`). HEAD `cc884ec` as at 2026-07-27, working tree clean.
- **Structure: a THREE-LANE ROUTER homepage** (rebuilt 19 Jul, resolves the old coaching-vs-AI positioning drift):
  - `/individuals` · `/workplaces` · `/research` · plus `/tools`
  - Old URLs preserved by 301s in `_redirects`: `/clients` → `/workplaces`, `/for-individuals` → `/individuals`, `/evidence` → `/research`, `/publications` → `/research#publications`, `/iron-protocol` → `/individuals#iron-guide`.
- **Checkout indirection:** `_redirects` holds a single swap point, `/buy/script-pack` → the live Stripe link. Change that one line if the storefront moves.

### What is live

```
✅ Iron Risk Check ......... /iron-risk-check · 17 items · presence-of-risk
                             triage · non-diagnostic educational report +
                             disclaimer · antenatal branch · Vinge et al. cited
   🔴 GATE-06 SOFT LAUNCH: needs ONE external person to complete it before
      it may enter outreach. Still zero as at 2026-07-27.
✅ Lead capture ............ Apps Script backend, deployed, tested end to end
✅ Branded email ........... receives (send-as outstanding)
✅ 14 pages ................ incl. two article pages and four thank-you pages
```

---

## 2. POSITIONING & OFFERS

- **Package A, consulting (THIS LEADS):** biostatistics, meta-analysis, statistical analysis plans, sample size, reproducible R pipelines, evidence synthesis. Buyers are research groups, biotech and medtech, CROs, med-comms and HEOR consultancies. **Rates and the full priced deliverable menu live in CANONICAL FACTS and `AU CONSULTING LANE (income now)`.**
  - 🔴 **KNOWN GAP:** `/research` PROVES he can do statistics but does not SELL statistics. Its entire commercial ask is "Book a call to talk about an industry or collaboration project". The fifteen-item priced menu sits in a private document. See §6 item 3.
- **Package B, screening builds:** program design, screening frameworks, evidence reviews for workplaces and occupational-health providers. Tiered pricing LOCKED in CANONICAL FACTS (founding pilot under A$15k / standard A$15-25k / premium A$25-40k). ⛔ Do not sign until PI insurance is bound.
- **Package C, products:** Iron Risk Check (free), R Biostatistics Script Pack (A$49), Wheel of Life (A$9), guides. Lemon Squeezy storefront.
- **Coaching (individuals):** scoped as 2 x 50-minute sessions plus a comprehensive wellness assessment and a 2-month program. **Not currently priced in CANONICAL FACTS.** The older Kickstart A$120 / Holistic A$199-per-month tiers predate the 19 Jul rebuild and should be treated as unconfirmed until re-decided.
- **Proof points:** 10+ years research · PhD UWA · **30+ research outputs** · work **cited by WHO** · screening reach **3,000 women** · featured ABC Radio / BJSM / JAMA Network Open / Healio / MedPage.
  - ⛔ **Numbers defer to CANONICAL FACTS.** Never "peer-reviewed" as the qualifier. Never 10,000 women. `$850K+ funding` and `34,000 members` were REMOVED 2026-07-02, do not reintroduce.
  - ⛔ **Never cite OSHA in iron-scoped copy.** OSHA cited the heat paper, not the iron work.

---

## 3. BRAND SYSTEM

- **Canonical:** `~/Documents/GitHub/drcwd-design-system/` (this repo) = v3 "Authority". Grape `#352051` + DM Serif Display / DM Sans, white-dominant editorial, evidence and stat motif, delta logo. Live visual home: claude.ai/design id `27287049-8ee5-4962-95f4-24d9cde8f6de`.
- Edit ONLY `colors_and_type.css` + `tokens.json`. Full spec in `README.md`, paste-context in `SKILL.md`.
- ⚠ As at 2026-07-27 the repo carries an **uncommitted modification to `colors_and_type.css`**. Resolve or commit it before treating the tokens as settled.

---

## 4. STOREFRONT / MONEY / DOMAIN

- **Payments:** Stripe (site CTAs) **and** Lemon Squeezy (products). ⚠ No stated rule for which rail handles what. Lemon Squeezy has shown an incomplete "Setup" badge, so payouts may not actually land. Verify before pointing anyone at a link.
- **Booking:** Google Calendar appointment scheduling, `calendar.app.google/J3FgoPCSGZgUym398`. ⛔ NEVER Calendly.
- **ABN:** registered (AU). GST **not** registered, which is correct below A$75k turnover. Quote GST-free and be visibly cheaper than institutional competitors. Compulsory within 21 days of crossing A$75k.
- 🔴 **NO TAX-INVOICE TEMPLATE EXISTS.** He cannot bill the day someone says yes. Open enabling task.
- 🔴 **NO PI INSURANCE BOUND.** Spec now known: PI A$5M / PL A$10M minimum. Quote through a professional-lines broker, **not** IICT (a complementary-therapies body, wrong scope for data and research consulting). Free to quote, bind on signature.

---

## 5. SOCIAL & DISTRIBUTION

- **LinkedIn** in/cory-dugan-phd · **IG** @dr.cwdugan · **FB** /dr.cwdugan · **X** @CoryDugan10 · GitHub portfolio.
- **Buffer** connected, free plan, 3 channels. ⚠ The B2B posting queue was deliberately KILLED 2026-07-22 in a social reset and replaced with educational holding content.
- ⚠ LinkedIn personalised invites: **0 of 3 remaining** for the month, spent 2026-07-12. The note cap is 200 characters, not 300.
- *(HolisticHer is LEGACY, archived to `Z_ARCHIVE/` on 2026-07-23. drCWDugan is the sole brand. Never mix design systems.)*

---

## 6. ⚠ KNOWN DRIFTS / RECONCILE BEFORE BUILDING

1. **[RESOLVED 2026-07-19] Host, DNS and email.** The site is on Cloudflare Pages, DNS is Cloudflare, and branded email receives. The 18 Jun entries claiming Netlify deploy, Squarespace DNS, no MX and a `-all` SPF were all false by 27 Jul. Corrected in §1.

2. **[RESOLVED 2026-07-14, shipped] IRON-5 name collision.** Renamed to **Iron Risk Check**. `/iron-5` and `/iron-5.html` both 301 to `/iron-risk-check`. ⛔ Never reintroduce "IRON-5" (Vinge et al., PMID 41916414, Lund). Citing the Vinge instrument by name is fine.

3. 🔴 **OPEN: `/research` is a credentials page, not an offer page.** The single highest-value fix available. Package A is the fastest lane to revenue and has no shopfront. A page edit, not a rebrand.

4. 🔴 **OPEN: `PUNCHLIST.md` in the website repo is STALE.** Last rewritten 5 Jul. It still leads with "BLOCKER: IRON-5 NAME COLLISION, this is unresolved" (it is resolved) and references `tools.html` in a pre-rebuild form. Update or retire it.

5. 🔴 **OPEN: Package B's wedge was FALSIFIED.** AU mining medicals run no routine bloods at all, so there is no ferritin result for a screening layer to act on. Rebuild the offer on the true premise before selling it again.

6. ⚠ **OPEN: one line on `individuals.html` sits close to a regulatory edge.** "I can help you read your pathology in context" is close to *pathology interpretation*, a clinical phrasing an unregistered provider should avoid. A one-line rewording into the literacy and advocacy register fixes it.

7. ⚠ **OPEN: `leads.json` has not been written to since 2026-07-14.** It is still the declared single source of truth for leads, but state has accumulated in the project store and the master tracker instead. Either revive it or formally retire it. Do not derive pipeline counts from its `stage` field: 89 of 99 records have it empty.

---

## 7. DISAMBIGUATION: "when Cory says X, here is what already exists"

| Cory says… | Reality | Likely intent |
|---|---|---|
| "build a landing page" | a full 14-page site exists at drcorydugan.com | (a) edit an existing lane page, (b) ADD a focused page, or (c) a standalone campaign page. **Ask which.** |
| "the website" | `drcwd-website` repo, branch `rebuild-cloudflare` → Cloudflare Pages | edit the existing repo, not a new build |
| "rebrand" / "a new domain" | a Layer 2 question serving the lowest-ticket package | usually NOT urgent. Read §0 first. |
| "update pricing / services" | edit the lane page; prices come from CANONICAL FACTS only | in-place edit and redeploy |
| "a new tool / questionnaire" | `drcwdugan-product-builder` skill; sold via Stripe or Lemon Squeezy | net-new product |
| "send outreach" | leads live in `leads.json`, unwritten since 14 Jul | ⚠ check the master tracker for current state, not just the store |

---

## 8. REGULATORY POSTURE (added 2026-07-27)

Derived from `BUSINESS 🟣/NEW GEMINI/Western Australia Health Business Manual.docx`, reviewed and corrected. Full review in `REVIEW - NEW GEMINI documents.md`.

```
                                    PACKAGE A   PACKAGE B   PACKAGE C
AHPRA title clarity / holding out       no         some        YES
HaDSCO Code of Conduct (WA)             no         some        YES
TGA Software as a Medical Device        no         maybe       YES
Privacy Act APPs (health service)       no*        YES         YES
PI insurance before signing          standard   ⛔ REQUIRED  ⛔ REQUIRED
```

\* A contracted statistician analysing a client's research dataset under the client's ethics approval is not providing a health service to the data subjects. Confirm with an adviser before relying on this in a contract.

**The three rules that matter most:**

1. **The TGA line.** Software stays unregulated while it is an educational compiler, a doctor-patient communication aid, or general wellbeing tracking. It becomes a regulated medical device if its primary purpose is to **diagnose or screen for a specific clinical condition**. ⛔ Never say a questionnaire "detects" anything. The live tool already says "it is not a test and it does not diagnose anything". Keep it that way, and re-test the FINAL copy every time, not the draft.
2. **AHPRA and "Dr".** "Doctor" is **not** a protected title. The requirement is that where "Dr" advertises a health service and does not refer to a registered medical practitioner, the qualification must be made **clear**. "PhD" currently appears on all 14 pages, so the clarity test appears met. Do not remove it.
3. **Privacy Act s6D(4).** The small-business turnover exemption is **revoked** for any entity providing a health service and collecting health data, regardless of turnover. Anything the lead capture stores needs Australian data residency, explicit consent, and no secondary use.

**Flagged, not yet actioned:** the HaDSCO Code of Conduct poster and complaints procedure are a **display** obligation on the website, not a filing obligation. Required before Package B or C trades in WA.

---

## 9. NAMES THAT ARE CLOSED

```
⛔ IRON-5 .................. Vinge et al., PMID 41916414 (Lund). Published,
                             validated, 5 items. Cory's tool is 17 items,
                             binary tier, no score. Renamed 14 Jul 2026.
⛔ "The Iron Lab" .......... collides with an AU supplement store, an AU
                             research-chemical supplier, and multiple gyms.
⛔ ironhealth.com.au, and the iron-brand space generally
     THE IRON CLINIC (theironclinic.com) was founded in 2015 by
     PROFESSOR TOBY RICHARDS, built on his research into iron deficiency
     and women's physical and mental health. It is the only CQC-registered
     dedicated iron infusion provider in the UK. THE IRON ACADEMY
     (theiron.academy) is its education arm.
     Toby Richards is Cory's PhD supervisor and a 10x co-author.
     Also occupied: Iron Health · The Iron Infusion Clinic (AU) ·
     ironiv.com.au · The Iron Infusion Centre (UK) · The Iron Suites ·
     Iron & Thyme Health Clinic (WA).
     → Closed on POSITIONING, not availability. Naming into a supervisor's
       established brand, in the same niche, reads as derivative to exactly
       the audience that matters most.
? "Dugan Research" ......... appeared in a 25 Jul Gemini prompt. Never
                             collision-checked. An undeclared candidate only.
```

**Note the pattern: two iron-name collisions in two weeks.** Any future name gets collision-checked before it reaches a document, let alone a domain purchase.

---

## 10. POISONED / SUPERSEDED

```
⛔ BUSINESS 🟣/NEW GEMINI/drCWDugan split 3 ways.docx
     A Gemini CHAT TRANSCRIPT, not a strategy document. It is the origin of
     the three-fold framing. Its copy carries an OSHA-in-iron-copy landmine,
     a "30 publications cited by WHO" compound overclaim, the banned word
     "validated", and "detect tissue-level iron depletion", which would void
     the TGA exclusion. SALVAGE the coaching scope only. Discard the copy.
⛔ The WA manual's invented revenue figures (D2C A$500-1,500, corporate
     A$10-50k/yr, SaaS A$20-150k/yr). Unsourced, and they contradict the
     LOCKED CANONICAL FACTS prices. CANONICAL FACTS wins, always.
⛔ Anything in BUSINESS 🟣/_archive/**
⛔ The .md lead lists as a STATUS source. They are narrative VIEWS only.
⛔ Stacey (the STACK AI) as a source of any number.
⛔ HolisticHer assets for any drCWDugan work.
⛔ netlify-deploy/ and any Netlify-era deploy instruction. The site moved.
```

---

*Prices, stats and credentials defer to `CANONICAL FACTS — drCWDugan (single source of truth)_CD.md`. Leads defer to `leads.json`, which is ⚠ unwritten since 2026-07-14, so check the master tracker for current state. Brand voice: Australian English, first-person singular, no emoji, no exclamation marks, NO EM DASHES anywhere.*
