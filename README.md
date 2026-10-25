# the-agent-crowd

> *A study of the popular mind — for your agent teams. Named after Gustave Le Bon's* The Crowd *(1895).*

**Independence engineering for multi-agent LLM systems.** A Claude Code skill plus a framework-agnostic playbook for keeping your agent team from behaving like a crowd.

English | [简体中文](README.zh.md)

## When to reach for this: the four gates

This skill exists only where a wrong verdict burns something other than a re-run.

| Gate | When | Cost of a wrong verdict |
|---|---|---|
| Acceptance gate | batch sign-off: ship / no-ship | a wrong green ships bugs to users |
| Decision gate | spec sign-off, merge to main, architecture choice | everything downstream gets reworked |
| External gate | public release, spending money, deleting data, outbound content | mistakes that cannot be taken back |
| Trust gate | about to change course on a collectively confident agent conclusion | a week burned on the wrong direction |

**One-line test: if this verdict turns out wrong, is the fix one more run — or does it burn someone else? One more run → this skill stays off. Burns someone else → keep reading.**

Inside the gates, tier by claim risk: cheap-to-rerun small pipelines use lightweight contracts (verbal confidence + spot checks); the five-line contract and full panels are reserved for verdicts that burn others.

## Three-symptom quick check

1. Near-identical wording across agents — especially when they repeat the same mistake.
2. All-green reports with no evidence trail.
3. Reports grow more confident with each hop — without adding new evidence.

Hit any one of the three and your agent legion is already turning into a mob.

## What & why

The name is borrowed from Gustave Le Bon's *The Crowd* (1895): his portraits of crowd failure — personal judgment collapses, emotion amplifies, errors are contagious, the most fluent speaker wins — have real counterparts in multi-agent systems. But the prescriptions here are not derived from him. The working evidence is LLM empirics — sycophancy, anchoring, correlated errors, context contamination — plus modern aggregation theory (Galton 1907; Condorcet 1785; Surowiecki 2004). Le Bon's mechanism claims about human crowds were revised by modern research (McPhail 1991; Postmes & Spears 1998); we borrow the failure narrative, never his mechanisms, conclusions, or politics.

The failure has a modern name: correlated errors. N agents launched with the same prompt and the same model are one judge with N copies of its errors — more agents do not mean more accuracy. Debate can make it worse: agents converge on a confidently biased consensus instead of correcting each other. The documented antidote is aggregation over independent judgments: Galton's 1907 ox-weighing crowd came within a pound of the true weight; Condorcet's jury theorem shows why independence is the load-bearing assumption; Surowiecki names independence as the line between a mob and a wise crowd.

Hence the two-domain doctrine: **Isolate for judgment. Share for construction.** Construction work (writing code, drafting docs) benefits from shared context; judgment work (reviewing, deciding, voting) collapses when judges share context. Everything here operationalizes that single distinction — and it is enforced only at the four gates above; everywhere else, run free.

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

Copy the whole `the-agent-crowd/` directory — it must include `SKILL.md` together with `references/`; copying `SKILL.md` alone breaks the relative links.

- project (recommended): `<your-project>/.claude/skills/the-agent-crowd/` — commit it with the project so every session and every parallel subagent inherits the discipline; teammates get it on clone.
- personal: `~/.claude/skills/the-agent-crowd/` — applies across all your projects.

The skill triggers at the four gates: acceptance sign-offs, decisions and merges, external releases, and moments of trusting an agent team's confident collective conclusion — or whenever an agent team converged on a confidently wrong answer.

### Other frameworks (CrewAI / LangGraph / AutoGen / ...)

Read `references/` as a methodology; there is no runtime dependency:

- [references/principles.md](references/principles.md) — the conceptual mapping and the citations
- [references/playbook.md](references/playbook.md) — copy-paste dispatch templates, handoff contract, debate moderation, merge checklist
- [experiments/protocol.md](experiments/protocol.md) — minimal reproducibility protocol to verify or falsify the mechanism claims (protocol defined; results pending)
- [examples/before-after.md](examples/before-after.md) — a worked case for calibrating your pipeline

A good first step: run the Pre-flight questions in [SKILL.md](SKILL.md) before your next gate dispatch.

## When NOT to use this

This skill exists only at the four gates. Every other moment: run full speed in parallel, share context, skip the ceremony. Construction with shared context beats N isolated constructors (Cognition 2025), and trivial checks where latency and cost dominate need no gate at all.

## Related work

Orchestration mechanics (parallel waves, dispatch, hooks) are well served by existing projects; the missing layer is judgment-independence discipline. Survey and positioning: [references/related-work.md](references/related-work.md).

## Sources

1. Le Bon, *The Crowd: A Study of the Popular Mind* (1895)
2. Galton, "Vox Populi", *Nature* (1907)
3. Condorcet jury theorem (1785); Surowiecki, *The Wisdom of Crowds* (2004)
4. Du et al., *Improving Factuality and Reasoning through Multiagent Debate* (2023) — arXiv 2305.14325 — https://arxiv.org/abs/2305.14325 — landing page: https://composable-models.github.io/llm_debate
5. Smit et al., *Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs* (ICML 2024) — https://arxiv.org/abs/2311.17371
6. *Debate or Vote: Which Yields Better Decisions in Multi-Agent Systems?* (2025) — https://arxiv.org/abs/2508.17536
7. *Emergence of Biased Consensus in Multi-Agent LLM Debates* (2026) — https://arxiv.org/abs/2608.02827
8. Cognition, *Don't Build Multi-Agents* (2025) — https://cognition.com/blog/dont-build-multi-agents
9. Anthropic, *How we built our multi-agent research system* (2025)
10. Sharma et al., *Towards Understanding Sycophancy in Language Models* (2023) — arXiv 2310.13548 — https://arxiv.org/abs/2310.13548
11. Chan et al., *ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate* (ICLR 2024) — arXiv 2308.07201 — https://arxiv.org/abs/2308.07201
12. McPhail, *The Myth of the Madding Crowd* (1991); Postmes & Spears, deindividuation meta-analysis, *Psychological Bulletin* (1998)

## Disclaimer

Le Bon's *The Crowd* (1895) is political commentary, not empirical science; its deterministic notions (such as the "race soul") have been abandoned by modern science — most directly in McPhail (1991) and the Postmes & Spears (1998, *Psychological Bulletin*) deindividuation meta-analysis. This repo borrows only his behavioral observations — deindividuation, contagion, suggestibility, the preference for illusion — as naming metaphor and failure narrative; the engineering prescriptions rest on LLM empirics and aggregation theory, and we adopt neither Le Bon's conclusions nor his politics.

## License

MIT — see [LICENSE](LICENSE).
