---
name: the-agent-crowd
description: Independence engineering for multi-agent LLM systems, derived from crowd psychology (Le Bon's The Crowd, 1895) and modern multi-agent research. Use when designing subagent orchestration, ensemble/debate workflows, or agent review pipelines; when dispatching reviewer/critic agents; or when an agent team converged on a confidently wrong answer. Triggers: multi-agent design, subagent dispatch, ensemble, debate, groupthink, 乌合之众, 从众, 独立评审.
---

# The Agent Crowd

Your agent team is a crowd. Le Bon (1895) showed what crowds do: individual
judgment collapses, emotion amplifies, errors are contagious, and the most
fluent speaker wins. LLM agents share none of humanity's excuses — no fatigue,
no face to lose, and they *run on* suggestion. A multi-agent system without
engineered independence is not an ensemble; it is one mind holding N copies of
its own biases.

## The Prime Directive

**Isolate for judgment. Share for construction.**

- Construction tasks (writing code, drafting docs) benefit from shared context —
  see Cognition's "Don't Build Multi-Agents" (2025).
- Judgment tasks (reviewing, deciding, voting) collapse when judges share
  context — see Le Bon and the multi-agent debate literature.
- Every rule below operationalizes one thing: independence between judges.

## The Seven Principles

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
Same-model votes correlate; a shared blind spot stays shared. For high-stakes
verdicts route independent reviews through different models or materially
different prompts; treat same-model concurrence as one vote, not two.
Smell: "three models agreed" when all three are the same model behind
different names.

### P4 — Blind the reviewer
Knowing the author, model, or framework makes reviewers lenient or hostile.
Strip author identity, model identity, and prior verdicts from the reviewer's
context; judge the artifact, not the pedigree.
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

1. Outputs from different agents use near-identical phrasing.
2. Unanimity arrived suspiciously fast.
3. All-green reports with no evidence trail.
4. Review quality tracks the author, not the artifact.
5. Debate conclusions drift toward whoever spoke first or loudest.
6. An error survived N review layers (they shared one blind spot).
7. Reports grow more confident with each pipeline hop.

## When NOT to use this

- Single well-scoped task: one agent with a good prompt beats coordination
  overhead.
- Construction where coherence matters more than judgment: keep shared
  context; do not blindly parallelize agents editing the same files.
- Trivial checks where latency/cost dominates.

## References

- [references/principles.md](references/principles.md) — full mapping, with citations
- [references/playbook.md](references/playbook.md) — copy-paste dispatch templates
- [references/related-work.md](references/related-work.md) — survey and research
- [experiments/protocol.md](experiments/protocol.md) — minimal reproducibility protocol (defined; results pending)
- [examples/before-after.md](examples/before-after.md) — worked example
