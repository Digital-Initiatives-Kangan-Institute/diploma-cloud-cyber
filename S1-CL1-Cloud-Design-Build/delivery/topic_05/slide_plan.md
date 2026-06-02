# Topic 5 — Making the case · Slide plan

*The single source for this Topic's teaching + exercise slides, in deck order. (Pairs with `coverage.md`, the UoC/AT spec, which is grounded in `planning/at1-presentation-uoc-coverage.md`.)*

**Depth ceiling.** Topic 5 teaches **communicating and defending** the finished business case at a board presentation — to the level of AT1 Part B (criteria B1–B9): build the deck, deliver the pitch, handle Q&A and secure sign-off. It does *not* re-teach the analysis (Topics 1–4) or slide-design tooling. Components: **C1→prepare & rehearse · C2→deliver · C3→handle the room.**

**Teaching source: all bespoke.** Communication skills — no AWS deck. Topics 1–4 are *applied* (the content presented; the knowledge defended in Q&A), not re-taught.

---

## AWS slides to add to `source_slides/`

**None.** Topic 5 is fully bespoke — the human-isolation step is a no-op and `source_slides/` stays empty.

---

## How to build the single deck

Walk this file top-to-bottom; each line is one slide, in final order. Same conventions as Topics 2–4: `[BESPOKE]` = author from the brief · `[EX]` = exercise slide.

**Exercise spine.** The component exercises run the **whole presentation cycle** on the **practice business case** (YAT Accounting System / Ledgerline) the student completed in Topics 2–4: **build & rehearse a board deck (C1) → deliver it to a mock board (C2) → field Q&A, capture feedback, get sign-off (C3)**. Mirrors AT1 Part B (8–10 slides; 10–15 min present + ~5 min Q&A; board role-played) on a different system.

**In-world rule.** Slides stay in-world: speak of "the board", "your business case", "the YAT Board Presentation Deck template"; don't tip which system is the *assessed* one. Keep the UoC / Part-B-criterion mapping in the **speaker notes** only.

---

### Opener

- **`[BESPOKE]`** From the written case to the room
```
Topic 5 — Making the case
A great business case still has to be sold. Now you present it to the board for the decision.
- The written case is done (Topics 2–4); this Topic is about communicating and defending it.
- Three moves: prepare & rehearse → deliver → handle the room (Q&A + sign-off).
- This is the presentation event — an observed assessment. HOW you present is assessed, not just what you built.
```

---

### C1 — From document to pitch  *(prepare & rehearse)*

- **`[BESPOKE]`** The pitch is a distillation, not a read-through
```
A board deck is not your business case with slide borders — the board read the document already.
The deck carries the spine (the ask, the money, the risk, the plan); you fill the rest verbally.
8–10 slides, one business-case section each, with speaker notes. Build it on the YAT Board Presentation Deck template.
```
- **`[BESPOKE]`** The board arc
```
Order the deck the way a board decides:
  Agenda → strategic context → current state → the gap → options → recommendation →
  cost summary → benefits → risks → implementation plan → the decision requested → Q&A.
One section per slide: headline + a few points. The recommendation and the plan get the airtime.
```
- **`[BESPOKE]`** What makes the cut
```
KEEP (a board needs it to decide): the ask · the cost comparison · the key risks + mitigations ·
  the plan · the strategic fit.
CUT (it lives in the document): line-item detail · method explanations · anything in the appendices.
If a slide doesn't help the decision, it's a handout, not a pitch slide.
```
- **`[BESPOKE]`** Rehearse — this is where pitches are won  *(emphasised)*
```
Preparation isn't done when the deck is built. REHEARSE:
  - run it aloud, walking the board through each slide — not reading it
  - time it (target 10–15 min); if you run long, cut
  - anticipate the board's questions (cost assumptions, risk, prioritisation, strategic fit) and prepare answers
  - practise stating the ask and asking for sign-off — the bit students most often fumble
A rehearsed pitch sounds confident; an unrehearsed one reads off the slides.
```
- **`[EX] [BESPOKE]`** Build & rehearse your board deck (Accounting engagement)
```
Build an 8–10 slide board deck for your practice Business Case (Accounting System / Ledgerline) on the
YAT Board Presentation Deck template, with speaker notes. Then REHEARSE it:
  - run it aloud and time it (target 10–15 min)
  - in your notes, write the three questions you'd least like to be asked — and your answers
Remember to: lead with the section spine; slides = headline + a few points; end on the decision requested.
⏱ ~30 min build + rehearse, then we present
```
- **`[BESPOKE]`** C1 takeaways
```
- The deck is a distillation — the spine, not the whole document.
- Board arc: context → gap → options → recommendation → cost/risk → plan → the ask.
- Preparation includes rehearsal: run it aloud, time it, prepare for the likely questions.
```

---

### C2 — Deliver the case

- **`[BESPOKE]`** Lead with the ask
```
A board listens better when it knows what you want. Open by naming the decision you're seeking,
then walk them through the case that justifies it. Don't hide the ask on the last slide.
```
- **`[BESPOKE]`** Walk the board through it
```
Deliver in order: report the situation and the gap, walk through how you evaluated the options
(the CBA + risk), and put the action plan — explicitly seeking the board's feedback and approval.
You're reporting to a superior and asking for a decision, not lecturing.
```
- **`[BESPOKE]`** Speak the board's language
```
The board is not technical. Plain English; translate each technical term as you use it
("RDS — a managed database the vendor runs for us"). Pitch complex ideas in business terms —
cost, risk, availability, continuity. Jargon loses the room.
```
- **`[EX] [BESPOKE]`** Deliver your pitch (Accounting engagement)
```
Present your board deck to a mock board (peers + trainer as Sam Walker / Pat Lin), 10–15 minutes.
Remember to:
  - open with the ask
  - walk context → gap → options → recommendation → cost/risk → plan
  - translate technical terms as you go; eyes on the room, not the slides
⏱ 10–15 min each, then feedback
```
- **`[BESPOKE]`** C2 takeaways
```
- Lead with the ask, then justify it.
- Report → evaluate → put the plan and seek approval.
- Plain English, technical terms translated, pitched to a non-technical board.
```

---

### C3 — Handle the room  *(Q&A, feedback & sign-off)*

- **`[BESPOKE]`** Q&A is assessed
```
The board's questions aren't a formality — they probe whether you understand your own analysis and
the cloud/evaluation principles behind it. Defend your case from your evidence; don't bluff.
```
- **`[BESPOKE]`** Listen, then answer
```
Use listening and questioning technique:
  - let the question land; clarify if unsure ("Do you mean cost or risk?")
  - answer directly, pointing to your evidence (your CBA, your risk register)
  - check it landed before moving on
A crisp "good question — here's the data" beats a long ramble.
```
- **`[BESPOKE]`** Be ready for these
```
The board probes across dimensions — prepare for:
  cost assumptions (what if pricing changes?) · risk (biggest reason to say no?) ·
  prioritisation (which change is riskiest?) · strategic fit (a second campus in Year 3?) ·
  service models + standards (why IaaS/PaaS here? which standards informed it?).
These come straight from your own Topics 1–4 work — defend, don't re-derive.
```
- **`[BESPOKE]`** Seek feedback & get sign-off
```
Close the loop:
  - explicitly seek and respond to the board's feedback (confirm you've understood it)
  - capture the feedback in the Feedback Record
  - obtain the board's sign-off on the action plan
The decision is the point of the whole exercise — ask for it.
```
- **`[EX] [BESPOKE]`** Run the Q&A + feedback + sign-off (Accounting engagement)
```
After each pitch, the mock board asks 3–5 questions, then gives feedback and signs off.
  Presenter: clarify → answer from your evidence → seek/respond to feedback → capture it → get the sign-off.
  Board: probe across the dimensions above.
⏱ ~5 min each, then debrief
```
- **`[BESPOKE]`** C3 takeaways
```
- Q&A tests your grasp of your own case — defend it from your evidence.
- Listen, clarify, answer directly, check it landed.
- Seek and respond to feedback, capture it, and obtain sign-off — always ask for the decision.
```

---

### Close

- **`[BESPOKE]`** From the practice room to the real thing
```
- You can now build a board deck, deliver it, and handle the room — the whole communication skill.
- That completes the case for the migration: analyse it, plan it, and sell it.
- You practised on the Accounting System; next you do it for real.
- Next: produce and present your real Business Case for the YAT LMS migration.
```

---

## Build notes

- **All bespoke, ~19 slides** (opener 1 · C1 6 · C2 5 · C3 6 · close 1) + 3 section dividers + title ≈ 23. No `source_slides/`, no image placeholders.
- **Exercise = the full presentation cycle** on the practice BC: build & rehearse (C1) → deliver (C2) → Q&A + feedback + sign-off (C3). Mirrors AT1 Part B on a different system.
- **Rehearsal is emphasised in C1** (its own teach slide + built into the C1 exercise) — per the coverage.
- **Teaching uses neutral/illustrative fragments** — the Q&A "be ready for these" dimensions are framed generically; students answer from their *own* Topics 1–4 work.
- **Inputs already on the website / in hand:** the YAT Board Presentation Deck template (Templates section) + a past board deck in the Document Archive (style reference) + the student's own completed practice BC (Topics 2–4). Nothing new to publish.
- **Canonical sources = the website** (`diploma-cloud-cyber-website`), not the stale `scenario/MIGRATED/` copies.
- **Speaker-note mapping (trainer):** C1 = `401 PC 4.1` (deck) [B4] + prep for B2/B3 · C2 = `517 PC 1.4` [B1], `517 PC 2.4` [B2], `517 PC 3.3` [B3], `401 PC 4.1` [B4], `517 FS Oral Comm` [B7], `502 FS Oral comm` [B9] · C3 = `401 PC 4.2` [B5], `502 PC 5.2` [B6], `517 FS Interact with others` [B5/B6], `517 FS Oral Comm` [B8], `502 FS Oral comm` [B9] + the Q&A probes (`517 PC 1.1/2.1/2.2/2.3/3.1/3.2`, `401 KE 1/3`, `502 PC 1.1/1.2`, `502 KE 1`). All → **AT1 Part B**.
