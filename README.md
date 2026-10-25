# the-agent-crowd

> *A study of the popular mind — for your agent teams. Named after Gustave Le Bon's* The Crowd *(1895).*

**Independence engineering for multi-agent LLM systems.** A Claude Code skill plus a framework-agnostic playbook for keeping your agent team from behaving like a crowd.

English | [简体中文](README.zh.md)

<!-- Status: draft. English copy pending professional review; README.zh.md is the canonical full version. -->

## Three-symptom quick check

1. Outputs from different agents are near-identical in wording.
2. All-green reports with no evidence trail.
3. Homogeneous language style across agents.

Hit any one of the three and your agent legion is already turning into a mob.

## What & why

In 1895, Gustave Le Bon watched individuals dissolve into crowds and described the mechanics: personal judgment collapses, emotion amplifies, errors are contagious, and the most fluent speaker wins. LLM agent teams recreate every one of those mechanics — without humanity's excuses. Agents do not tire, do not lose face, and literally run on suggestion. A multi-agent system without engineered independence is not an ensemble; it is one mind holding N copies of its own biases.

The failure has a modern name: correlated errors. N agents launched with the same prompt and the same model are one judge with N copies of its errors — more agents do not mean more accuracy. Debate can make it worse: agents converge on a confidently biased consensus instead of correcting each other. The antidote is old and well documented: Galton's 1907 crowd nailed the ox weight because the guesses were independent; Condorcet's jury theorem shows why independence is the load-bearing assumption; Surowiecki names the dividing line plainly — interacting crowds (Le Bon's) versus aggregated isolated judgments.

Hence this repo's Prime Directive: **Isolate for judgment. Share for construction.** Construction work (writing code, drafting docs) benefits from shared context; judgment work (reviewing, deciding, voting) collapses when judges share context. Everything here operationalizes that single distinction.

## The 7 principles

| Principle | Failure it prevents | Smell test |
|---|---|---|
| P0 Independence before quantity | Counting agents instead of independent judges (correlated errors) | You raised agent count hoping accuracy would rise |
| P1 Quarantine verdicts | Upstream conclusions become "facts" in downstream prompts; hallucination compounds along the chain | A prompt says "as agent A confirmed, X is correct" |
| P2 The orchestrator speaks last | The dispatcher's hunch anchors every reviewer | "I think this is almost done, just double-check" in a dispatch |
| P3 Heterogeneity over homogeneity | Same-model votes correlate; shared blind spots stay shared | "Three models agreed" — all the same model behind different names |
| P4 Blind the reviewer | Reviewers turn lenient or hostile based on author/model pedigree | Verdicts track the author's seniority, not the artifact's quality |
| P5 Evidence over fluency | Confident green reports trusted for tone, not checks | An all-green report nobody can trace to a command output |
| P6 Keep the dissent | Minority dissent pressured into consensus; the dissenter saw the bug | A debate where everyone converged, no minority position recorded |

Full mapping from crowd mechanics to engineering countermeasures, with citations: [references/principles.md](references/principles.md).

## Quick start

### Claude Code

Copy the skill into a skills directory:

- personal: `~/.claude/skills/the-agent-crowd/SKILL.md`
- project: `<your-project>/.claude/skills/the-agent-crowd/SKILL.md` — commit it with the project so every teammate's and every agent session inherits the discipline.

The skill triggers on multi-agent design, subagent dispatch, ensemble/debate workflows, and review dispatches — or whenever an agent team converged on a confidently wrong answer.

### Other frameworks (CrewAI / LangGraph / AutoGen / ...)

Read `references/` as a methodology; there is no runtime dependency:

- [references/principles.md](references/principles.md) — the conceptual mapping and the citations
- [references/playbook.md](references/playbook.md) — copy-paste dispatch templates, handoff contract, debate moderation, merge checklist
- [experiments/protocol.md](experiments/protocol.md) — minimal reproducibility protocol to verify or falsify the mechanism claims (protocol defined; results pending)
- [examples/before-after.md](examples/before-after.md) — a worked case for calibrating your pipeline

A good first step: run the Pre-flight questions in [SKILL.md](SKILL.md) before your next multi-agent dispatch.

## When NOT to use this

- Single well-scoped task: one agent with a good prompt beats coordination overhead.
- Construction where coherence matters more than judgment: keep shared context; do not blindly parallelize agents editing the same files.
- Trivial checks where latency/cost dominates.

## Related work

Orchestration mechanics (parallel waves, dispatch, hooks) are well served by existing projects; the missing layer is judgment-independence discipline. Survey and positioning: [references/related-work.md](references/related-work.md).

## Sources

1. Le Bon, *The Crowd: A Study of the Popular Mind* (1895)
2. Galton, "Vox Populi", *Nature* (1907)
3. Condorcet jury theorem (1785); Surowiecki, *The Wisdom of Crowds* (2004)
4. Du et al., *Improving Factuality and Reasoning through Multiagent Debate* (2023) — arXiv 2305.14325, https://arxiv.org/abs/2305.14325; landing page: https://composable-models.github.io/llm_debate
5. Smit et al., *Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs* (ICML 2024) — https://arxiv.org/abs/2311.17371
6. *Debate or Vote: Which Yields Better Decisions in Multi-Agent Systems?* (2025) — https://arxiv.org/abs/2508.17536
7. *Emergence of Biased Consensus in Multi-Agent LLM Debates* (2026) — https://arxiv.org/abs/2608.02827
8. Cognition, *Don't Build Multi-Agents* (2025) — https://cognition.com/blog/dont-build-multi-agents
9. Anthropic, *How we built our multi-agent research system* (2025)

## Disclaimer

Le Bon's *The Crowd* (1895) is political commentary, not empirical science; its deterministic notions (such as the "race soul") have been abandoned by modern science. This repo borrows only his behavioral observations — deindividuation, contagion, suggestibility, the preference for illusion — and adopts neither his conclusions nor his politics.

## License

MIT — see [LICENSE](LICENSE).
