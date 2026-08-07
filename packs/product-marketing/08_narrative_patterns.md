---
doc: packs/product-marketing/08
title: Narrative patterns
status: active
version: 0.1.0
updated: 2026-08-07
owners: [story-producer]
---

# 08 — Narrative patterns

Five structures that work, what each is for, how long it runs, and the way each one
characteristically fails. These are defaults, not a permission list. A brief may
depart from them and says why.

The reason to have defaults at all: marketing video is made in volume against
deadlines, and a team without a structure to reach for will reach for "list the
features over music", which is the format that performs worst in every genre and
gets made most often.

## 1. Choosing a pattern

The brief names one, at [gates.yaml](gates.yaml) `brief_approval`, before scripting.
Choose by what the viewer already knows and what you want them to do next.

| The viewer… | Pattern | Runs |
|---|---|---|
| does not know the product exists | [Launch film](#2-launch-film) | 60–120 s |
| knows it exists, does not know what one part does | [Feature explainer](#3-feature-explainer) | 45–90 s |
| has bought it and is stuck | [Onboarding and how-to](#4-onboarding-and-how-to) | 30–180 s |
| believes the product works, doubts it works *for them* | [Case study](#5-case-study) | 90–180 s |
| wants to see it before deciding | [Demo](#6-demo) | 2–5 min |

**One pattern per piece.** The most reliable way to produce something nobody watches
is to make a launch film that also explains three features and includes a customer
quote. Each of those is a different piece with a different audience and a different
next action.

## 2. Launch film

**For:** an audience that does not know the thing exists. The job is to make them
want to know more — not to make them understand everything.

**Structure:**

| Beat | Function | Share |
|---|---|---|
| **The tension** | A situation the audience recognises as their own. Concrete and specific. Not a problem statement — a moment. | 15–20% |
| **The turn** | The product enters. One clear reveal. | 10% |
| **The demonstration** | Two or three capabilities, shown working, at the level of *what it lets you do* rather than *how it works*. Captured, per [06_product_depiction.md](06_product_depiction.md) §1. | 40–50% |
| **The consequence** | What is different now. The version of the viewer's day that this produces. | 15–20% |
| **The ask** | One action. | 5% |

**Rules:** the tension is specific enough that the wrong audience knows it is not for
them. Every capability shown is a `product_claim`. The film shows what ships today
unless the studio's roadmap policy says otherwise
([05_claim_substantiation.md](05_claim_substantiation.md) §5).

**How it fails:** *the tension is generic.* "Work is hard. Teams are busy." Every
product could open that way, so it introduces nothing and the viewer has learned
nothing by the reveal. The second failure is **the feature list wearing a launch
film's coat** — six capabilities at eight seconds each, none of which lands. Two shown
properly beat six shown fast, every time.

## 3. Feature explainer

**For:** an audience that already has the product or has decided to consider it, and
needs one specific thing made clear.

**Structure:** the job the feature does → the situation before it → the feature
working, end to end, without cuts that hide steps → what changed → where to find it.

**Rules:**

- **One feature.** The name of the pattern is doing work.
- **Show the whole path.** The most common reason an explainer fails to convert is
  that it skipped the two steps the viewer would have got stuck on. If a step is
  boring, that is information about the product, not about the edit.
- **Real capture, real states.** Loading, empty, and error states are part of the
  path. Removing them is prohibited under
  [06_product_depiction.md](06_product_depiction.md) §3.3.
- **Where to find it** is the beat teams drop for time and the one that determines
  whether the feature gets used.

**How it fails:** *it explains the mechanism instead of the job.* A viewer does not
want to know how the sync engine resolves conflicts; they want to know that their
colleague's edits will not overwrite theirs. Mechanism is interesting to the people
who built it, which is why it survives internal review.

## 4. Onboarding and how-to

**For:** someone who has already paid, is inside the product, and is stuck right now.
This is the only pattern whose audience is actively frustrated, and the entire craft
follows from that.

**Structure:** state the outcome in the first five seconds → the steps, in order, at
the pace of someone following along → the confirmation of success → the one thing
that commonly goes wrong.

**Rules:**

- **Front-load the outcome.** "By the end of this you will have connected your
  calendar." A viewer who cannot tell in five seconds whether this is their problem
  leaves.
- **Pace for following, not watching.** Slower than feels right in the edit. The
  viewer is doing it while watching.
- **Chapter it**, and title chapters by task. This is the format most often entered
  from a search result, mid-way.
- **Version it visibly.** The interface will change. Record the build on every shot
  ([06_product_depiction.md](06_product_depiction.md) §3) so that when the UI moves,
  the affected videos are a list rather than a discovery.
- **No music bed loud enough to compete with instruction.** Captions carry more of
  this format than any other; core requires them regardless.

**How it fails:** *it is made by someone who knows the product too well.* They skip
the click that is obvious to them, and the video becomes useless at exactly the point
where the viewer needed it. The fix is procedural, not editorial: have someone who has
never done the task follow the cut, and watch where they stop.

## 5. Case study

**For:** an audience that believes the product works and does not believe it works in
their situation. The job is recognition, not proof.

**Structure:** who they are and why the viewer should see themselves in them → the
situation before, in their words → what they did → what changed, with a figure they
stand behind → what they would tell someone considering it.

**Rules:**

- **The customer speaks.** [06_product_depiction.md](06_product_depiction.md) §6
  governs the whole format: real customer, their words, release before the shoot
  covering AI processing, employer permission for marks and premises.
- **Specific beats impressive.** A customer describing the exact hour of the week
  they got back is more persuasive than a percentage, and cheaper to substantiate.
- **Every figure they state is an `E-CUS` claim**, attributed to them on screen, never
  restated by the narrator as a general fact
  ([05_claim_substantiation.md](05_claim_substantiation.md) §4).
- **Choose a customer the audience resembles.** A case study about an organisation
  ten times the viewer's size proves the opposite of what it intends.
- **Let the before be real.** A sanitised before makes the after unbelievable.

**How it fails:** *it becomes a brand film about the customer.* Beautiful footage of
their office, a warm quote about partnership, and nothing about what actually changed.
The test at review: **can a viewer state what the customer's problem was, and what is
different now?** If not, the piece is a testimonial with a budget.

## 6. Demo

**For:** someone evaluating. Longest and least decorated of the five, and the one
where craft is mostly restraint.

**Structure:** the shape of the product in thirty seconds → one realistic workflow,
end to end → two or three secondary capabilities in context → limits and fit → next
step.

**Rules:**

- **One coherent workflow beats a tour of the navigation.** Evaluators are trying to
  imagine their own work in it. A tour of menus gives them nothing to imagine.
- **Real data volumes.** A demo on three records tells an evaluator nothing about a
  product they will run on thirty thousand, and if it slows down at that scale, they
  will find out. Honestly seeded data, per
  [06_product_depiction.md](06_product_depiction.md) §3.1.
- **Say what it does not do.** The most trust-generating thirty seconds available in
  this genre. An evaluator who discovers a limit themselves discounts everything else
  you said; one you told them extends credit to the rest.
- **Timings are performance claims.** If the demo shows something completing, the
  elapsed time is asserted. Speed changes are disclosed
  ([06_product_depiction.md](06_product_depiction.md) §3.3).
- **Chaptered and re-enterable.** Demos are scrubbed, not watched.

**How it fails:** *it is the product team's happy path at their speed.* Every field
pre-filled, every choice already made, nothing that resembles the mess an evaluator
brings. It reads as a product that has never met a customer.

## 7. Cutdowns and variants

Every pattern above produces derivatives — 6-second, 15-second, vertical, square,
silent, thumbnail-first. Treated as a pattern in their own right, with three rules:

1. **Cut down from an approved master, never sideways from an unapproved edit.** The
   master's approvals and claim substantiation flow to its derivatives; a variant cut
   from a work-in-progress carries none.
2. **A cutdown can create a claim its master did not make.** Removing a qualifier,
   dropping the conditions from a performance figure, or ending on the result instead
   of the caveat all change what is asserted. Claim substantiation is checked on
   **every variant**, per [07_brand_and_message.md](07_brand_and_message.md) §5.
3. **Composition survives reframing or the variant does not exist.** Interface and
   qualifiers are checked in every aspect ratio at picture lock, per
   [gates.yaml](gates.yaml).

## 8. What none of these are

- **Not a documentary.** If a piece makes claims about history, an industry, or
  society, those claims need [documentary-history](../documentary-history/)'s
  evidence chain, not this pack's
  ([05_claim_substantiation.md](05_claim_substantiation.md) §1).
- **Not fiction.** A dramatised scenario is permitted and is plainly dramatised.
  A performer in a scenario is not a customer
  ([06_product_depiction.md](06_product_depiction.md) §7).
- **Not a substitute for the product working.** Every pattern above assumes the thing
  exists and does what the film shows. That assumption is the whole content of
  [05_claim_substantiation.md](05_claim_substantiation.md), and no structure rescues
  a piece that violates it.

## 9. Inheritance and enforcement

Adds to core; loosens nothing. The structures here are craft guidance and carry no
exemptions: every pattern is bound by
[../../core/01_provenance_and_ai_disclosure.md](../../core/01_provenance_and_ai_disclosure.md) §2,
by [../../core/02_rights_and_licensing.md](../../core/02_rights_and_licensing.md),
and by [../../core/03_distribution_and_formats.md](../../core/03_distribution_and_formats.md)
for every variant it produces.

| Standard | Gate | Mechanism |
|---|---|---|
| §1 | `brief_approval` | Pattern named on the brief; one message, one audience, one action |
| §2–§6 craft rules | `picture_audio_lock` | Reviewed against the named pattern's failure mode |
| §7 | `claim_substantiation`, `picture_audio_lock` | Every variant checked, not the master alone |
| §7.1 | `stakeholder_approval` | Approval is on a specific version, and derivatives name their master |

Checklists: [../../ops/checklists/](../../ops/checklists/). Gate definitions: [gates.yaml](gates.yaml).
