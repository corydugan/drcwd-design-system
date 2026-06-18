# drCWDugan Design System v3 — Session Handoff & Resume

**Session:** 2026-06-18 (STACK workshop: Claude Design best practices)
**State:** Phase 1 complete + system locked + logo built. Mid Phase 2.

---

## 1. WHAT THIS IS (one paragraph)
Rebuilt the drCWDugan brand design system from scratch as **v3 "Authority"** during a STACK workshop on design-system best practices. Kept the locked constraints (grape `#352051`, DM Serif Display + DM Sans, white-dominant editorial) and elevated the system to read as a **healthcare-AI consultant/founder** rather than a wellness coach. Caught and documented a single-source-of-truth drift (the old claude.ai/design project was still TEAL, predating the 2026-06-12 grape rebrand) — fixing that drift is *why* v3 exists, and it's now under git version control so it can't happen silently again.

## 2. WHERE EVERYTHING LIVES (canonical)
| Thing | Location |
|---|---|
| **Source of truth (edit ONLY here)** | `~/Documents/GitHub/drcwd-design-system/` → `colors_and_type.css` + `tokens.json` |
| GitHub repo (private) | https://github.com/corydugan/drcwd-design-system |
| Live Claude Design project | "Dr. Cory Dugan Design System v3 (Authority)" · id `27287049-8ee5-4962-95f4-24d9cde8f6de` |
| Full spec (human-readable) | repo `README.md` (8 blocks) |
| Paste-into-tools context | repo `SKILL.md` |
| Logo files | repo `logo/*.svg` |
| **SUPERSEDED — do not edit** | old grape-v2 at `00_ACTIVE/03_BUSINESS 🟣/DR.CWD/dr-cory-dugan-design-system/` · old TEAL claude.ai project (id `d1f1b3fe-...`) |

## 3. DISCOVERABILITY (so any future session knows what this is)
Registered in 4 places — all done:
- ✅ Global `~/.claude/CLAUDE.md` — brand-system line rewritten to point at v3 (loads every session)
- ✅ Memory `project_drcwd_design_system_v3.md` + MEMORY.md index line
- ✅ Project JSON — Business/Income brand-build project (`auto_holisticher_drcwdugan_ai_build_20260521`): notes pointer + session logged; dashboard rebuilt
- ✅ Drive pointer — `DR.CWD/BRAND SYSTEM v3 (canonical) — READ ME.md`

## 4. WORKSHOP PROGRESS (9 steps)
```
PHASE 1 — BUILD (Claude Design)
 1 Connect Buffer ............. ✅ already connected
 2 Bring brand in ............. ✅ extracted from existing grape system
 3 Photo bank ................. ◐ PENDING — your 6 real photos to migrate into v3
 4 Build system .............. ✅ v3, 8 blocks
 5 Refine .................... ✅ direction = healthcare-AI authority
 6 Lock into one spec block .. ✅ (README.md + chat block)
 7 Hand to Claude Code ....... ✅ repo + tokens are the source
PHASE 2 — GENERATE
 8 Generate asset ............ ◐ IN PROGRESS — logo done; landing/IG/prototype pending
 9 Reuse / batch ............. ☐ later
```

## 5. TASK + SUBTASK LIST
### ✅ DONE
- [x] Author v3 files: `colors_and_type.css`, `tokens.json`, `README.md`, `SKILL.md`, 4 preview cards
- [x] Build live Claude Design v3 project (8 files)
- [x] git init + commit + push to private GitHub repo
- [x] Register for cross-session discoverability (CLAUDE.md, memory, project JSON, Drive pointer)
- [x] Lock the system into one clean spec block
- [x] Build the LOGO: primary / credential / stacked wordmarks + monogram icon (grape + inverse) + logo sheet; pushed to Claude Design + GitHub

### ◐ OPEN — decide on resume
- [ ] **Refine the logo** (workshop step 5 — don't accept first pass). Open decisions:
  - [ ] Monogram letters: lowercase **"cd"** (current) vs uppercase **"CD"** vs **"CWD"** (matches @dr.cwdugan handle)
  - [ ] Data-baseline mark under the name — keep as signature / dial up / drop?
  - [ ] Eyebrow text "HEALTH-SCREENING AI" vs alt (e.g. "WOMEN'S HEALTH · AI")
  - [ ] Outline the SVG fonts to paths before any print use (currently live web-font text)
- [ ] **Photo bank (step 3):** migrate the 6 real owned photos (headshot, lab-testing, iron-screening, pennington-talk, panel-discussion, abc-radio) from the OLD Claude Design project into v3 → completes the image library
- [ ] **Next Phase 2 asset** (pick one): 
  - [ ] Landing page — book-a-call / capture-email for health-screening consulting (hero → proof/stats → offer → CTA → footer); deployable to drcorydugan.com via Netlify
  - [ ] Instagram templates — feed/carousel/story w/ editable copy slots → push via connected Buffer
  - [ ] Clickable prototype — e.g. IRON-5 screener flow (onboarding → input → evidence-cited result)
- [ ] **Retire the old copies** — delete/archive the old grape-v2 folder + old teal claude.ai project so there's genuinely one of everything

## 6. KEY DESIGN FACTS (so you don't re-derive)
- **Authority elevation = data rigor, not new color.** v3 additions: `--ink-max` near-black, grape data-viz ramp, tabular `.stat` display, mono evidence voice, evidence motif (`.method-label` / `.data-baseline` / `.citation`), wordmark + PhD lockup, integrations block.
- **Logo idea:** every lockup carries the grape data-baseline rule = the same mark under stats, so the logo IS the evidence signature.
- **Voice:** AU English, first-person, no emoji, no exclamation marks, always cites the number.
- **Phase 2 prompts** (from workshop) live in the chat / workshop notes: Instagram, Website, Logo, Prototype — each says "inherit tokens, don't invent; then list which tokens used where."

## 7. FIRST ACTION ON RESUME
Open the live system to review the logo, then decide §5 open items:
`claude.ai/design` → "Dr. Cory Dugan Design System v3 (Authority)". Tell Claude: "resume the drCWDugan design system — refine the logo" or "build the landing page."
