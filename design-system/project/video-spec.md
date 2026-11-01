# Video spec

The opening and closing every drCWDugan video carries, the screen rules, and the voice. It is written so a code-generating tool (Google AI Studio, a render script) can implement it without seeing anything else. The brand book's Video section is the summary; this is the detail. Brand voice guidelines v2.2 govern the words; where anything here disagrees with them, they win.

Every colour below is a token in this design system's `tokens.json`. The render code lives in the `drcwd-social-assets` repository under `women-health/` (`reels-20260818/build.py`, `series.py`) and in `~/.claude/scripts/podcast_reel/` (`signature.py`, `build_reel.py`).

---

## 1. The rule

**Every video opens on a title card and closes on the drCWDugan sign-off.** No exceptions. A clip that ships without both is not finished.

The opening card states what the viewer is about to watch. The sign-off is the signature, and it is the same four beats every time, so people come to recognise it before the name is legible.

---

## 2. The surface

Video uses the INK surface, never the paper one. Ink is a peer surface in this brand, not a dark mode, so do not derive it by inverting light values.

    field / background      #0B0B0C     ink-max      surface
    primary text            #FFFFFF     paper        surface-fg
    secondary text          #E4E5E7     ink-200      surface-fg-muted
    tertiary / captions     #C8CACE     ink-300      surface-fg-subtle
    hairline rules          #2A2A2D     ink-900      surface-rule
    accent, TYPE ONLY       #8A6FB8     grape-500    surface-accent
    eyebrow micro-caps      #8A6FB8     grape-500    surface-eyebrow
    the sign-off mark       #FFFFFF     paper        surface-logo

**grape-800 #352051 is the primary brand grape on the paper surface and it never appears as type on ink.** It dies on a near-black field. On ink the accent and the eyebrow are grape-500, and grape-500 is the rare colour, spent by hand rather than sprinkled. White on grape-500 is large text only (24px or more).

When a colour fades, fade it toward the FIELD colour, not toward white or toward transparent-over-white. On a near-black field that difference is the difference between a fade and a glow.

---

## 3. The type

    display / headlines     DM Serif Display, regular weight, tracking -0.02em
    everything else         DM Sans, regular / medium / bold
    a number on its own     IBM Plex Sans regular, font-figures (Cory, 26 October 2026)

All three faces are on Google Fonts. **DM Sans has no tabular-figures table**, so any `font-variant-numeric: tabular-nums` on it is a silent no-op and columns of numbers will not line up. A number standing on its own is set in IBM Plex Sans; a number inside a sentence stays in DM Sans.

Never letterspace DM Serif Display positive. Never use DM Serif Display below about 36px on a 1080-wide frame; it is a display face and it falls apart small.

---

## 4. The opening card

Canvas 1080 x 1920, field #0B0B0C. Three elements, stacked, centred.

    EYEBROW     y 286   DM Sans Bold 32px   #8A6FB8   the series label
                        e.g. "The Iron Panel · 01"
    TITLE       y 342   DM Serif Display 82px   #FFFFFF
                        The subject. One line.
    SUBTITLE    y 466   DM Sans regular 38px   #C8CACE
                        One short line saying what it is in plain words.

**The title shrinks to fit, never clips.** Try 82px, then 74, then 66, then 58, and use the first size whose measured width is under 930px. A title such as "Total iron-binding capacity" overruns at the display size, and getting cut at both edges is the failure this rule exists to stop.

Timing, in seconds from the start of the card:

    0.2 - 1.4   eyebrow fades in
    0.5 - 1.9   title fades in
    1.6 - 2.8   subtitle fades in
    hold, then the card clears over 0.5s before the content starts

Use a smoothstep curve for every fade, `t * t * (3 - 2t)`. Nothing in this brand moves linearly and nothing bounces.

---

## 5. The sign-off

Cory's call, 29 September 2026.

    the mark    delta + drCWDugan, white on ink (the Logos group's
                "drCWDugan lockup ink"; the render uses wordmark.png)
    placement   small, at the bottom right of the area TikTok and Instagram
                keep clear of their buttons and captions, NOT the frame's
                corner, which both apps cover
    duration    1.5 s in total
    address     NONE. No web address and no handle under the mark
    sound       nothing spoken over it

The approved render is `drCWDugan signature_09292026_CD.mp4` in the Motion group: 1.5 s, 1080 x 1920, 24 fps, approved by Cory on 29 September 2026. No show logo on the end card of any reel from that date.

### The four beats

Smoothstep throughout, in this order:

    0.00 - 0.39   triangle outline draws, apex first, by arc length
    0.36 - 0.55   triangle fills, overlapping
    0.52 - 0.82   wordmark wipes left to right, hard edge
    0.82 - 1.04   grape rule grows from the centre of the group
    1.04 - 1.50   hold

- **The triangle draws itself.** A single continuous white stroke travels around the outline from the apex and returns to it. Truncate the path by ARC LENGTH, not by vertex count; truncating per vertex makes the pen hesitate at the corners. It is not a fade and not a scale-up.
- **The triangle fills** underneath the stroke, alpha 0 to 255, before the outline has finished closing.
- **The wordmark wipes** column by column, left to right, with a hard vertical edge. The letters do not move; they are uncovered where they already are. Render the wordmark as an image with the triangle REMOVED from it and animate the triangle in code, or the two fight over alignment and the result is a double delta.
- **The grape rule** (3px, #8A6FB8) grows outward from the centre of the group, symmetrically, never sweeping from one side.

### Placement, measured 29 September 2026 against both platforms' own guides

    TikTok      In-Feed Standard safe zone template (ads.tiktok.com, "TikTok
                Auction In-Feed Ads", Feed.png 2880 x 5120, scaled to 1080 x 1920):
                safe x 120 to 960 for y 240 to 840, then x 120 to 780 for
                y 840 to 1260. The right rail of buttons owns x 780 and beyond.
    Instagram   Meta Ads Guide, Instagram Reels: at least 14% of the top,
                35% of the bottom and 6% on each side kept free:
                safe x 65 to 1015, y 269 to 1248.
    BOTH        bottom-right corner of the shared safe area is x 780, y 1248.

So the sign-off sits as far bottom right as both apps allow, 8 px inside that corner.

    scale          0.8 of the lockup units
    group          x 448 to 772, right-aligned to x 772, y 1154 to 1239
    triangle       apex (466.7, 1157.0), base (448.3, 1190.6) to (485.1, 1190.6)
    wordmark.png   drCWDugan, top-left (503.0, 1155.6), 269 x 47
    grape rule     y 1238, x 448.3 to 772, 3 px, #8A6FB8, grows from x 610

Checked by drawing it over TikTok's template and Meta's margins: nothing crosses either line.

---

## 6. Handing over to and from the content

Do not hard-cut between the content and either card. **Crossfade 0.4 seconds.** A hard cut from lit footage to a near-black field reads as a fault rather than a transition.

If the content carries audio and the cards do not, give the cards a silent stereo track at 48kHz before joining, or the concatenation will refuse the mismatched stream layout.

---

## 7. Rules for everything on screen

- **No em dashes and no en dashes.** Anywhere. Use a comma, brackets, or a full stop.
- **Never the banned words** in the voice guidelines' Never-use table. Machine-check every string with `style_gate.py --au`.
- **Australian spelling.** haemoglobin, anaemia, coeliac, colour, organise.
- **A number on screen passes the evidence check first:** checked against a named source, and a prevalence always with its threshold. The Iron Panel series goes further and puts no number on screen; other videos may show a checked, sourced number (voice guidelines, Video).
- Every scientific claim carries a citation in the source file, even though the citation never appears on screen.

---

## 8. Acceptance checks

A video is finished when all of these pass:

1. Frame is 1080 x 1920. Output frame rate is stated and consistent.
2. The opening card's title is fully visible, not clipped at either edge.
3. The sign-off runs all four beats, in order, in 1.5 s, at the bottom right of the shared safe area, and the final frame is the completed mark with no web address and no handle.
4. No grape-800 #352051 appears as type on the ink field.
5. Every transition into and out of a card is a crossfade, not a cut.
6. A text search of every string in the video finds no em dash, no en dash, and none of the banned words.
7. If the file carries audio, the sign-off is silent of speech, and the final narrated word ends at least 0.3 seconds before the sign-off begins.
8. If the file carries audio, exactly one question is spoken over the opening card, it is not printed on screen, and the episode answers it.

---

## 9. Voice over, and the last seconds

### Whose voice

Two lanes, Cory's call, 29 September 2026:

- **Educational reels** (explainers, the Iron Panel, concept animations): **Kore**, Gemini text to speech, through `~/.claude/scripts/voiceover.py`, where Kore is the hardcoded default. The locked narrator voice; do not audition others.
- **Podcasts, talks, interviews and in-person footage:** Cory's own voice, as recorded.

Voiceover scripts are written for the ear, separately from the on-screen captions. In the Iron Panel series, `S.narrate()` in `series.py` holds on-screen captions with start and end times, so the script and its timings already exist; a voice track is a read of those slots, not a new writing job.

### The last seconds

**Nothing is spoken over the sign-off. Not the name, not an address.** The sign-off is a signature, and a signature is silent.

    the final narrated line       spoken
    the on-screen closing card    spoken, after a pause of about 0.4s
    a beat of silence             about 0.4s
    the sign-off                  SILENT, all four beats, 1.5 s

If a music bed is used it may continue under the sign-off and should resolve on the final frame. It must not start there, because a bed arriving at the sign-off reads as an advert break.

### Iron Panel episode 1, written out

    18.2 - 21.4   "Haemoglobin only falls once the store is gone."
    21.8 - 24.8   "The store runs down, long before the blood does."
    24.8 - 25.2   silence
    25.2 onward   the sign-off, silent, 1.5 s

The line at 21.8 is the one already on screen as the closing card. Speaking it is the only doubling permitted in the whole video, because it is the thesis and it is the line people screenshot.

### The closing line of every Iron Panel episode

| Episode | The line |
|---|---|
| 01 ferritin | The store runs down, long before the blood does. |
| 02 serum iron | It rises after a meal, and drifts across the day. |
| 03 TSAT | A low share is one of the two ways deficiency is called. |
| 04 TIBC | So the room goes up while the iron on board does not. |
| 05 transferrin | Learn the carrier and three of them stop being separate. |
| 06 haemoglobin | Anaemia is where the shortage ends, not where it starts. |
| 07 sTfR | It is less disturbed by inflammation than ferritin is. |
| 08 MCV | A red cell lives for months, so this one moves last of all. |
| 09 hepcidin | Inflammation raises it, whether or not you need what is behind it. |
| 10 ZPP | The wrong molecule builds up, and counting it is the test. |
| 11 CRP | CRP is what tells you which of the two you are looking at. |

These lines, and the questions in section 10, are the August 2026 build. On 13 October 2026 episodes 02 and 04 to 10 were rebuilt in the explainer format (`~/Documents/drcwd-reels/iron-panel-NN-*/`), every script went through the evidence check, and some lines did not hold, episode 02's "drifts across the day" among them. The rebuilt scripts carry the current lines; check a line against them before reusing it.

### Reading direction

Read down, not up. These are statements of how something works, not announcements. The last word of each line is where the pitch drops. Leave the pause before the closing line longer than feels comfortable, because that pause is what makes the line land rather than merely arrive.

---

## 10. The opening question

The opening card names the subject. It does not say why anyone should stay, and in a vertical feed the first two seconds are the whole retention problem.

**Do not read the card aloud.** The eyebrow, title and subtitle are on screen, large, for three seconds. Instead, ask ONE question over the card. It is spoken, never on screen, so the card stays clean and the viewer gets two channels rather than one.

    0.0 - 3.0   the opening card
    0.5 - 2.8   the question, spoken over it
    3.0         narration begins

### The rule for writing one

- It is a QUESTION, and the episode answers it. If the episode does not answer it, it is a hook, and hooks are not this brand.
- It comes out of that episode's own closing line, worked backwards. The closing line is the answer, so the question is whatever that answer settles.
- No number, no prevalence, no threshold. Section 7 applies to spoken words too.
- Second person. "Your iron", not "the patient's iron".
- One sentence. Two at most, and then only if the first is short.
- Do not answer it in the question. "Did you know ferritin falls first?" is a statement wearing a question mark.

### The eleven Iron Panel questions

| Ep | Spoken over the card |
|---|---|
| 01 ferritin | When your iron starts running out, which number moves first? |
| 02 serum iron | Why can the same blood give two different iron results in one day? |
| 03 TSAT | Your iron is being carried somewhere. How much of that carrying is actually being used? |
| 04 TIBC | Why does one number on your iron panel go up when you are running out? |
| 05 transferrin | Three lines on your panel are readings of the same protein. Which three? |
| 06 haemoglobin | If your haemoglobin came back normal, are you in the clear? |
| 07 sTfR | Which iron marker still works when you are inflamed? |
| 08 MCV | What does the size of a red cell tell you about the iron that built it? |
| 09 hepcidin | What decides whether the iron you swallow ever gets in? |
| 10 ZPP | What does a red cell do when it cannot find the iron it needs? |
| 11 CRP | Your ferritin came back normal. Can you trust it? |

Each is answered inside its own episode by the closing line in section 9.

---

## 11. The voice decision

### Where it stands

    the voice       KORE, for every educational reel (Cory, confirmed 9 September 2026)
    the platform    Gemini TTS, model gemini-2.5-flash-preview-tts (shipped 28 August 2026)
    the mechanism   ~/.claude/scripts/voiceover.py, Kore its hardcoded default
    the detail      the "The Voice" tab of NOTEBOOKLM_BUSINESS/OUTREACH AND SOCIAL MEDIA.gdoc

On 28 August 2026 Cory ran a six-voice test through Gemini TTS and picked Kore over Erinome, which read as English rather than neutral, over Charon, Algieba, Sadachbia and Iapetus, which were male-leaning, and over Sulafat, which ran long and buried the sign-off.

The 19 August 2026 plan named Google Cloud Text-to-Speech, Chirp 3 HD, en-AU female. That platform has never produced a second of audio: measured 9 September 2026, the Cloud Text-to-Speech API returned HTTP 403 (not enabled in the project), and Cory declined to enable it. Kore survived the platform change because Gemini TTS and Chirp 3 HD share the same voice-family names.

### The 19 August 2026 research, kept as a record

Three passes: platform landscape, licensing of free tiers, and the evidence on accent and gender.

**Ruled out at the time, and why**

| Platform | Reason |
|---|---|
| ElevenLabs free | Non-commercial by its own terms, and requires "elevenlabs.io" in the title of the post. Upgrading later does not clear audio made on the free tier. |
| Azure Speech F0 | Product terms grant output rights to the paid tier only. |
| Murf free | Cannot export a file at all. |
| Coqui XTTS, F5-TTS | Weights are non-commercial even though the code is permissive. |
| Kokoro, Piper | Licences are clean, but neither ships an Australian voice. |
| Amazon Polly "Olivia" | The fallback with clean terms, native en-AU; not needed. |

**The accent.** General Australian. In a study of Australian listeners rating English accents, General Australian scored positively across both status and solidarity; Broad Australian and second-language accents rated more negatively. So the contrast that matters is General versus Broad, not Australian versus British versus American. Do not over-invest in this: the founding accent-and-credibility result did not replicate, and the mechanism with the best support is processing fluency, which argues for audio clarity rather than for a nationality.

**The female voice.** The evidence is thin and contested; one unreplicated conference paper, not a health outcome. Do not treat "women trust women's voices" as established. The choice is defensible on brand grounds, not on evidence.

**The finding to act on first.** Every comparable channel that works uses a named human on camera, not a synthetic narrator, and clinician-made videos draw a share of views well above their share of videos. The assumption worth breaking is not which synthetic voice; it is synthetic voice versus Cory's face. Second to that, caption quality has real peer-reviewed support for comprehension and retention, and accent does not: hand-corrected captions beat voice selection as an investment.

**What to test rather than assume**

- Same script, three voices: General Australian, British, General American. Measure three-second hold, average watch time, saves.
- General Australian versus Broad Australian.
- Synthetic narrator versus Cory on camera.
- Hand-written captions versus auto-captions, voice held constant.
