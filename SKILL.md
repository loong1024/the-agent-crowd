---
name: the-agent-crowd
description: Gate discipline for high-stakes agent verdicts, built on LLM empirics (sycophancy, anchoring, correlated errors, context contamination) and aggregation theory (Galton / Condorcet / Surowiecki); crowd psychology supplies the naming metaphor only. Use at acceptance gates (ship / no-ship), decision gates (spec sign-off, merge to main, architecture choice), external gates (public release, spending, data deletion, outbound content), or trust gates (about to act on an agent team's collectively confident conclusion); when dispatching reviewer/critic agents at one of these gates; or when an agent team converged on a confidently wrong answer. Triggers: 验收, 发布, 合并, 拍板, 架构选型, review dispatch, groupthink, 乌合之众, 从众, 独立评审.
---

# The Agent Crowd

Your agent team is a crowd. Le Bon (1895) claimed that in crowds individual
judgment collapses, emotion amplifies, errors are contagious, and the most
fluent speaker wins — we borrow that as a naming metaphor and a failure
narrative, not as an evidence base. LLM agents share none of humanity's
excuses: no fatigue, no face to lose, and a downstream agent defers to the
tone and confidence of whatever arrives from upstream. A multi-agent system
without engineered independence is not an ensemble; it is one mind holding N
copies of its own biases.

**Positioning.** The engineering prescriptions in this repo are not derived
from Le Bon. The working evidence is LLM empirics — sycophancy, anchoring,
correlated errors, context contamination, information cascades (Sharma et al.
2023) — plus modern aggregation theory (Galton 1907; Condorcet 1785;
Surowiecki 2004). Le Bon's *The Crowd* supplies the naming metaphor and the
failure narrative: the ailments he described have real counterparts in
multi-agent systems, but his mechanism claims about human crowds were revised
by modern research (McPhail 1991; Postmes & Spears 1998). We borrow the
narrative — never his mechanisms, conclusions, or politics.

## When to activate: the four gates

This skill exists only at four gates — the moments where a wrong verdict burns
something other than a re-run:

1. **Acceptance gate** (batch sign-off, ship / no-ship): a wrong green ships
   bugs to users.
2. **Decision gate** (spec sign-off, merge to main, architecture choice): a
   wrong call means everything downstream is reworked.
3. **External gate** (public release, spending money, deleting data, outbound
   content): a mistake here cannot be taken back.
4. **Trust gate** (about to change course because an agent team's conclusion is
   collectively confident): a wrong trust burns a week.

**The one-line test: if this verdict turns out wrong, is the fix one more run,
or does it burn someone else? One more run → this skill stays off. Burns
someone else → keep reading.**

Exemption inside the gates (claim-risk tiering): where re-runs are cheap and
the claim is small, use lightweight contracts — verbal confidence plus spot
checks. The five-line handoff contract and the full panels are reserved for
verdicts that burn someone else.

## The two-domain doctrine

**Isolate for judgment. Share for construction.**

- Construction tasks (writing code, drafting docs) benefit from shared context —
  see Cognition's "Don't Build Multi-Agents" (2025).
- Judgment tasks (reviewing, deciding, voting) collapse when judges share
  context — see the multi-agent debate literature.
- Every rule below operationalizes one thing: independence between judges.

## The seven principles — why the gate discipline works

### P0 — Independence before quantity
N same-prompt same-model agents are one judge with N copies of its errors
(correlated errors). Count independent judges, not total agents.
Smell: you raised agent count hoping accuracy would rise.

### P1 — Quarantine verdicts
An upstream agent's conclusion placed in a downstream prompt becomes "fact";
hallucination compounds along the chain. Pass artifacts (files, data, logs),
not conclusions; every handoff claim carries source + confidence.
Smell: a prompt says "as agent A confirmed, X is correct."

### P2 — The orchestrator speaks last
The dispatcher's hunch inside a reviewer prompt anchors every reviewer.
Dispatch prompts contain facts-of-task only ("review X against Y"), never the
orchestrator's own expectation; the orchestrator discloses its opinion only
after independent verdicts are in.
Smell: "I think this is almost done, just double-check" in a review dispatch.

### P3 — Heterogeneity over homogeneity
Same-model votes correlate; a shared blind spot stays shared. Heterogeneous
models lower correlation — they do not zero it (different models still share
training corpora and RLHF conventions), and they shift scoring criteria, so
anchor the merge with a rubric plus calibration examples. Treat same-model
concurrence as one vote, not two.
Smell: "three models agreed" when all three are the same model behind
different names.

### P4 — Blind the reviewer
Strip author identity and model identity from the reviewer's context — but
keep the spec and intent documents, or a bug becomes indistinguishable from a
recorded design tradeoff. Low-risk verdicts may waive blinding altogether.
Smell: review verdicts track the author's seniority, not the artifact's quality.

### P5 — Evidence over fluency
Confident fluent reports ("✅ all passed") are the most contagious artifact in
a pipeline; downstream trusts tone, not checks. Require checkable evidence per
claim (command output, file:line, metrics); use graded states
(pass/fail/blocked/skipped/unverified), never a bare boolean green.
Smell: an all-green report nobody can trace to a command output.

### P6 — Keep the dissent
Group formats pressure minority dissent into consensus; the lone dissenter is
often the only one who saw the bug. Collect verdicts privately before any
exchange; the merged report must quote dissent and why it was overruled.
Smell: a debate where everyone converged and no minority position is recorded.

## Workflow

1. **Pre-flight** (before dispatching): Which steps are judgments, not
   construction? Are the judges zero-context? Did any orchestrator opinion
   leak into a dispatch? Do two same-model agents share a vote? Can dissent
   be recorded?
2. **Dispatch**: use templates in references/playbook.md.
3. **Handoff**: every inter-agent claim uses the Claim/Evidence/Confidence/
   Source/Owner contract.
4. **Merge**: the orchestrator merges verdicts, quotes dissent, and never
   issues a bare green.

## Red Flags — you are running a mob, not a team

1. Outputs from different agents are near-identical in wording and wrong in
   the same way.
2. Unanimity arrived suspiciously fast.
3. All-green reports with no evidence trail.
4. Review quality tracks the author, not the artifact.
5. Debate conclusions drift toward whoever spoke first or loudest.
6. An error survived N review layers (they shared one blind spot).
7. Reports grow more confident with each pipeline hop.

## When NOT to use this

This skill exists only at the four gates. Every other moment: run full speed
in parallel, share context, skip the ceremony. Construction with shared context
beats N isolated constructors (Cognition 2025), and trivial checks where
latency and cost dominate need no gate at all.

## References

- [references/principles.md](references/principles.md) — full mapping, with citations
- [references/playbook.md](references/playbook.md) — copy-paste dispatch templates
- [references/related-work.md](references/related-work.md) — survey and research
- [experiments/protocol.md](experiments/protocol.md) — minimal reproducibility protocol (defined; results pending)
- [examples/before-after.md](examples/before-after.md) — worked example
