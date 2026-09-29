# Visualisation Compendium

Working catalogue of every insert-menu visualisation type, transcribed from
screenshots of the editor's insert menu.

Source app: **Gamma** (gamma.app). Basis, recorded 2026-08-14: Cory is
building the Lectures on Tap lecture deck in Gamma, and the menu structure in
the screenshots matches. Not independently checked against a labelled Gamma
UI, so treat the label as high confidence rather than settled.

In use by: `LIFE/DETERMINISM LECTURES ON TAP/08142026 Full Lecture Deck Gamma
PROMPT_CD.txt`, which names elements from this file card by card.

Nothing in this file is inferred. Every entry below was read off a screenshot.

Captured: 2026-08-14. Confirmed entries: 108 (14 charts, 47 smart layouts, 3 diagrams, 44 smart diagrams).

Edited 2026-09-28 on Cory's comments: the partial Toggle and Power BI rows, the gaps list, the naming traps and the three questions were removed, and a worked example was added to every entry. The published page is https://claude.ai/artifact/W8D1anckLY1YeCRfFYG1ez.

---

## 1. Charts (data marks)

| # | Name | Encoding | Reads well when | Fails when | Example |
|---|------|----------|-----------------|------------|---------|
| 1 | Line chart | position on a continuous x, usually time | trend and rate of change matter | categories are unordered | Use it for change over time, e.g. mean ferritin at each study visit across a year. |
| 2 | Area chart | line plus filled magnitude | a single cumulative total over time | several series overlap and occlude | Use it for one running total over time, e.g. total clinic enrolments building month by month. |
| 3 | Column chart | vertical length | comparing values across few categories | more than roughly a dozen categories | Use it for comparing a few categories, e.g. new referrals from each of five clinics. |
| 4 | Stacked Column chart | length split by sub-category | part-to-whole within each time point | comparing the middle segments across columns | Use it for part of a whole at each time point, e.g. each quarter's consults split into new and returning patients. |
| 5 | Bar chart | horizontal length | category labels are long | the axis is time | Use it for categories with long names, e.g. how many survey respondents reported each of eight named symptoms. |
| 6 | Stacked Bar chart | horizontal length split | part-to-whole with long labels | reading any segment other than the baseline one | Use it for part of a whole with long labels, e.g. each symptom split into mild, moderate and severe. |
| 7 | Pie chart | angle | two or three slices, one dominant | more than three slices, or comparing two pies | Use it for two or three parts of one whole, e.g. trial completers against withdrawals. |
| 8 | Donut chart | angle with a hole | same as pie, centre used for a total | same as pie | Use it for two or three parts with the total in the middle, e.g. oral against intravenous iron, with the number treated in the centre. |
| 9 | Combo chart | two encodings, dual axis | a count and a rate share an x axis | the second axis is chosen to manufacture a crossing | Use it for a count and a rate on one timeline, e.g. monthly tests as columns with the positive rate as a line. |
| 10 | Scatter chart | x and y position | association between two continuous variables | n is small enough to mislead | Use it for two continuous measures, e.g. ferritin against haemoglobin, one point per participant. |
| 11 | Bubble chart | x, y, plus area | a third magnitude genuinely matters | area is read as radius, inflating differences | Use it when a third quantity matters, e.g. clinics placed by cost and wait time, sized by patient volume. |
| 12 | Heatmap chart | colour on a grid | dense matrices, two categorical axes | the palette is not perceptually uniform | Use it for a dense two-way grid, e.g. deficiency rates by age band and by region. |
| 13 | Funnel chart | descending width | a genuine sequential drop-off | stages are not nested subsets | Use it for a nested drop-off, e.g. screened, eligible, randomised, completed. |
| 14 | Waterfall chart | running total with deltas | decomposing a change into contributions | contributions are not additive | Use it for splitting a change into its parts, e.g. how a monthly budget moves from income through each expense line. |


## 2. Smart layouts (structure, not data)

These carry no quantitative encoding. They are containers for text, so the
choice is about hierarchy and reading order, not about accuracy.

| # | Name | Shape it implies | Example |
|---|------|------------------|---------|
| 1 | Large bullets | flat list, few items, high emphasis | Use it for a few key points, e.g. three signs of iron deficiency on an opening slide. |
| 2 | Small bullets | flat list, more items, lower emphasis | Use it for a longer list, e.g. eight foods rich in iron. |
| 3 | Arrow bullets | list with an implied direction or progression | Use it for a list that moves forward, e.g. the steps from first symptom to diagnosis. |
| 4 | Solid boxes | parallel peers, equal weight, filled | Use it for equal options, e.g. three treatment routes side by side. |
| 5 | Solid boxes with icons | parallel peers with a category marker | Use it for equal options that each need a marker, e.g. four services, each with its own icon. |
| 6 | Outline boxes | parallel peers, lighter visual weight | Use it for equal points kept visually quiet, e.g. the three aims of a study. |
| 7 | Side line boxes | peers with a coloured left rule, boxed | Use it for separate findings, e.g. three key results, each in its own panel. |
| 8 | Side line text | peers with a left rule, no box | Use it for short takeaways, e.g. three lines of interpretation under a chart. |
| 9 | Top line text | peers with a rule above, no box | Use it for themes laid across a slide, e.g. the four themes of a lecture. |
| 10 | Top circle boxes | peers with a circular marker on top, often numbered steps | Use it for numbered stages, e.g. the four stages of a clinic visit. |
| 11 | Joined boxes | connected sequence, a chain or process | Use it for a linked sequence, e.g. referral, blood test, review, treatment. |
| 12 | Joined boxes with icons | connected sequence with category markers | Use it for a linked sequence with a marker per stage, e.g. the patient journey with an icon at each step. |
| 13 | Leaf boxes | peers with a rounded or organic container | Use it for a softer, less clinical set of points, e.g. wellbeing topics in a community talk. |
| 14 | Quote boxes | attributed text, pull quotes | Use it for attributed words, e.g. two client testimonials with their names. |

### 2b. Content blocks and process

Continues the same menu. Contiguity with "Quote boxes" above is not confirmed;
there may be entries between the two runs.

| # | Name | Shape it implies | Example |
|---|------|------------------|---------|
| 15 | Process steps | ordered stages, numbered | Use it for an ordered procedure, e.g. five steps to prepare for an iron infusion. |
| 16 | Labeled boxes | box with a header label per item | Use it for defined terms, e.g. ferritin, transferrin saturation and haemoglobin, each with a one-line definition. |
| 17 | Images with text | image paired with a caption block | Use it for people or places, e.g. team members, each with a photo and a short bio. |
| 18 | Icons with text | icon paired with a text block | Use it for benefits or features, e.g. four reasons to test, each with an icon and one line. |
| 19 | Timeline | events along an axis | Use it for dated events, e.g. the milestones of a research project from funding to publication. |
| 20 | Minimal timeline | events along an axis, reduced chrome | Use it for a few dated events on a clean slide, e.g. four career milestones. |
| 21 | Minimal timeline with boxes | same, items in containers | Use it for dated phases that need a note each, e.g. project phases with a short description under each. |
| 22 | Arrows | directional flow between items | Use it for cause and consequence, e.g. low intake leading to low stores, then to fatigue. |
| 23 | Pills | short labels as rounded tags | Use it for keywords, e.g. the topic tags for a talk. |
| 24 | Speech bubbles | quoted or attributed voice | Use it for voices, e.g. the questions patients most often ask. |
| 25 | Slanted labels | angled label treatment | Use it for a few bold terms, e.g. the headline words on a section divider. |

### 2c. Stat tiles

These display numbers without an axis or a scale. They read as figures, not as
comparisons, so they carry the risk of a magnitude with no reference point.
Pair each with its denominator or its source in the adjacent text.

| # | Name | Shape it implies | Example |
|---|------|------------------|---------|
| 26 | Stats | plain number plus label | Use it for one headline figure, e.g. a figure with its label and its source written beside it. |
| 27 | Circle stats | number inside a ring, often a proportion | Use it for a proportion, e.g. the share of participants who completed the trial, with the denominator stated in the text. |
| 28 | Bar stats | number with a horizontal bar | Use it for a headline percentage, e.g. a response rate, with the exact value in the text. |
| 29 | Star rating | ordinal rating out of five | Use it for a rating, e.g. how a client scored a consultation. |
| 30 | Dot grid stats | count or proportion as a dot matrix | Use it for a count out of a hundred, e.g. how many in every hundred women screened were deficient. |
| 31 | Dot line stats | count or proportion along a single line of dots | Use it for a count out of ten, e.g. how many in every ten patients returned for follow-up. |

### 2d. Step and stair forms

| # | Name | Shape it implies | Example |
|---|------|------------------|---------|
| 32 | Staircase | ascending stages, implies growth | Use it for levels that build on each other, e.g. the tiers of a membership program. |
| 33 | Steps | discrete stages, vertical | Use it for stages of a plan, e.g. the phases of a treatment plan. |
| 34 | Box steps | discrete stages in containers | Use it for stages that each need a note, e.g. onboarding steps for a new client. |
| 35 | Arrow steps | stages joined by arrows | Use it for a strict sequence, e.g. the steps of a lab protocol. |
| 36 | Steps with icons | stages with a category marker each | Use it for a sequence with a marker per step, e.g. book, test, results, follow-up. |
| 37 | Pyramid | hierarchy by tier width, apex at the top | Use it for a ranked hierarchy, e.g. levels of evidence from case reports up to systematic reviews. |
| 38 | Vertical funnel | narrowing sequence, top to bottom | Use it for narrowing an idea, e.g. from a broad topic down to one research question. |
| 39 | Cycle | closed loop, no start or end | Use it for a repeating loop, e.g. plan, do, study, act. |

### 2e. Radial and circular forms

Contiguity between "Cycle" and "Flower" is not confirmed.

| # | Name | Shape it implies | Example |
|---|------|------------------|---------|
| 40 | Flower | petals radiating from a centre | Use it for factors around one outcome, e.g. six causes of fatigue around the word fatigue. |
| 41 | Circle | items arranged on a circumference | Use it for members around a centre, e.g. the care team arranged around the patient. |
| 42 | Ring | items on a ring, centre left open | Use it for services around a theme, e.g. the parts of a clinic offering around its name. |
| 43 | Semi-circle | items on a half arc | Use it for a spread of options, e.g. four treatment choices along an arc. |
| 44 | Circle stats with middle bold line | ring stat, emphasis rule inside | Use it for one proportion that needs extra weight, e.g. the completion rate on a results slide. |
| 45 | Circle stats with external bold line | ring stat, emphasis rule outside | Use it for one proportion that needs extra weight, e.g. the follow-up rate on a summary slide. |
| 46 | Alternating boxes | items staggered left and right | Use it for a story told in turns, e.g. a project history alternating left and right. |
| 47 | Solid box small bullets | filled box containing a compact list | Use it for a boxed summary, e.g. the key recommendations at the end of a talk. |

## 3. Diagrams

A separate type label in the menu, distinct from "Smart layout". A `/diagram`
slash command is visible alongside this group.

| # | Name | Notes | Example |
|---|------|-------|---------|
| 1 | Blank diagram | empty canvas, build your own | Use it for anything the menu lacks, e.g. a custom participant flow diagram. |
| 2 | Weekly calendar | seven-day grid | Use it for a week's schedule, e.g. the sessions of a workshop week. |
| 3 | Gantt chart | tasks against a time axis, the only genuinely quantitative item in this group | Use it for tasks against dates, e.g. the work packages of a project across a year. |

## 4. Smart diagrams

A third type label, again distinct. These are relationship and metaphor shapes,
not data marks. None of them encodes a magnitude.

| # | Name | Shape it implies | Example |
|---|------|------------------|---------|
| 1 | Semi circle road | a journey along an arc | Use it for a path with stages, e.g. a career path from PhD to industry. |
| 2 | Target | nested rings, a goal at the centre | Use it for one goal with actions around it, e.g. a single research aim and its supporting work. |
| 3 | Minimal road | a journey along a line | Use it for milestones on the way to a launch, e.g. the steps to opening a clinic. |
| 4 | Linear venn | overlapping sets in a row, outlines | Use it for where fields meet, e.g. research, clinical practice and teaching. |
| 5 | Linear venn filled | the same, filled | Use it for where fields meet, filled for emphasis, e.g. data science, medicine and business. |
| 6 | Diamonds | peers as rotated squares | Use it for a set of values, e.g. the four values of a brand. |
| 7 | Minimal funnel | narrowing sequence, decorative | Use it for a narrowing idea, e.g. how a literature search goes from broad to focused. |
| 8 | Connected circles | linked nodes | Use it for linked ideas, e.g. the concepts a lecture ties together. |
| 9 | Concentric circles | nesting or containment | Use it for levels of influence, e.g. individual, family, community, society. |

Contiguity between "Concentric circles" and "Funnel 3d" is not confirmed.

| # | Name | Shape it implies | Example |
|---|------|------------------|---------|
| 10 | Funnel 3d | narrowing sequence, rendered with depth | Use it for a conceptual funnel, e.g. awareness, interest, booking. |
| 11 | Road | a journey along a path | Use it for a journey, e.g. a patient's route from first symptom to recovery. |
| 12 | Isometric building | stacked tiers drawn in projection | Use it for layers of a system, e.g. data, analysis and reporting in a data platform. |
| 13 | Isometric globe | a sphere in projection, reach or scope | Use it for international reach, e.g. the countries a project works in. |
| 14 | Isometric dashed squares | tiles in projection | Use it for modules, e.g. the units of a course. |
| 15 | Gears | interlocking parts, mutual dependency | Use it for parts that drive each other, e.g. diet, absorption and blood loss acting together. |
| 16 | Pillar | supports holding something up | Use it for supports of a whole, e.g. the three pillars of a strategy. |
| 17 | Orbit | satellites around a centre | Use it for partners around a hub, e.g. collaborating organisations around one project. |
| 18 | Venn diagram | overlapping sets | Use it for an overlap of two ideas, e.g. the skills shared by statisticians and clinicians. |
| 19 | Chain | linked sequence, each depending on the last | Use it for a causal chain, e.g. heavy periods leading to iron loss, then to low stores. |
| 20 | Bullseye | nested rings, a target at the centre | Use it for audiences in rings, e.g. core, secondary and wider audiences for a campaign. |
| 21 | Ribbon arrows | flowing directional sequence | Use it for a flowing sequence, e.g. the arc of a presentation. |
| 22 | Ideas | ideation cluster | Use it for brainstormed topics, e.g. ideas for a content series. |
| 23 | Inputs | several sources feeding one thing | Use it for sources feeding one output, e.g. surveys, lab results and records feeding one analysis. |
| 24 | Quadrant | two crossed axes, four regions | Use it for sorting into four groups, e.g. tasks by urgent and important. |
| 25 | Swoosh | curved directional sweep | Use it for momentum toward a goal, e.g. the direction of a business plan. |
| 26 | Versus | two things opposed | Use it for a head-to-head comparison in words, e.g. oral against intravenous iron. |
| 27 | Infinity | a two-lobed continuous loop | Use it for two things that feed each other, e.g. research and practice. |
| 28 | Square arrows | boxed directional sequence | Use it for a short boxed process, e.g. four steps in a referral. |
| 29 | Puzzle | interlocking pieces forming a whole | Use it for parts of a complete whole, e.g. the pieces of a care plan. |
| 30 | Bubbles | circles of varying size, scattered | Use it for a loose cluster, e.g. related topics around a talk. |
| 31 | Nested diamond | containment in rotated squares | Use it for a core inside a wider offer, e.g. a flagship service within a clinic's range. |
| 32 | Packed circles | circles filling a space | Use it for topics grouped within a theme, e.g. subtopics of women's health. |
| 33 | Arrow bars | bars with directional heads | Use it for progress shown as a picture, e.g. several goals moving forward, with no values implied. |
| 34 | Pinwheel | radial blades around a hub | Use it for areas around one idea, e.g. four domains around a central plan. |
| 35 | Iceberg | visible part above, hidden bulk below | Use it for what is seen against what is hidden, e.g. diagnosed cases above, undiagnosed cases below. |
| 36 | Slope | rise or decline along an incline | Use it for a stated direction, e.g. a plan for steady improvement. |
| 37 | Hot air balloons | items rising at different heights | Use it for goals at different stages, e.g. projects in planning, underway and launched. |
| 38 | Solar system | a centre with orbiting satellites | Use it for a main item with related ones around it, e.g. a core product and its add-ons. |
| 39 | Signs | signposts pointing in directions | Use it for choices at a decision point, e.g. the options after a diagnosis. |
| 40 | Circle hero | a single circular focal element | Use it for one message, e.g. the single takeaway of a talk. |
| 41 | Note collage | scattered note cards | Use it for many short inputs, e.g. comments collected in a workshop. |
| 42 | Impact | emphasis burst around one item | Use it for one striking finding, e.g. the headline result of a study. |
| 43 | Oval | a single oval focal element | Use it for one framed statement, e.g. a mission statement. |
| 44 | Arch | an arch as the framing shape | Use it for a framed title, e.g. the name of a program on its opening slide. |

Entries 40 to 44 read as framing and hero shapes for a single element rather
than relationship diagrams, unlike the rest of this section.

Contiguity is unconfirmed at four joins in this run: after "Chain", after
"Quadrant", after "Pinwheel", and after "Signs".

## Chart choice, one screen

```
QUESTION                          GOES TO
change over time                  line, area
compare categories                column, bar
part of a whole, few parts        pie, donut
part of a whole, over time        stacked column
two continuous variables          scatter, bubble if a third matters
a dense two-way matrix            heatmap
a total broken into drivers       waterfall
a nested sequential drop-off      funnel
a count and a rate together       combo
```

Moved 2026-09-28 from ~/.claude/references/ into this repository beside the page, on Cory's call, so the page and its text record version together.
