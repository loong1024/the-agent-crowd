# Related Work:相关开源项目与研究文献

## 一、相关开源项目调研

编排一个多 agent 系统的「机械层」——怎么并行、怎么派活、怎么收拢——已有不少成熟方案。本仓库不重复它们,填的是它们之上的「判断独立性纪律」层。

| 项目 | 定位 | 与本仓库的关系 |
|---|---|---|
| [am-will/swarms](https://github.com/am-will/swarms) | 多 agent 编排 skill:并行波次 + 编排者 | 提供派活的机械层;本仓库约束被派者「脑子里没有别人的答案」,可叠加使用 |
| [barkain/claude-code-workflow-orchestration](https://github.com/barkain/claude-code-workflow-orchestration) | hook 式委派框架 | 提供委派的触发与流转;本仓库补充委派时的上下文纪律(盲审 / 证据 / 分级) |
| [github/spec-kit issue #4128](https://github.com/github/spec-kit/issues/4128) | 社区对 agent 隔离协议的诉求 | 同类需求的公开信号:隔离协议是普遍痛点,本仓库给出纪律层的一个具体答案 |

**结论**:编排「机械层」已有成熟方案,「判断独立性纪律」层目前近乎空白。本仓库与上述工具是互补而非竞争关系:它们负责把活派出去,本仓库负责保证被派出去的每个评审,收到的上下文里没有别人的答案。可与上述工具叠加使用。

## 二、研究文献清单

1. Le Bon, *The Crowd: A Study of the Popular Mind* (1895)
2. Galton, "Vox Populi", *Nature* (1907)
3. Condorcet 陪审团定理 (1785);Surowiecki, *The Wisdom of Crowds* (2004)
4. Du et al., *Improving Factuality and Reasoning through Multiagent Debate* (2023) — https://composable-models.github.io/llm_debate
5. Smit et al., *Should We Be Going MAD? A Look at Multi-Agent Debate Strategies* (ICML 2024) — https://arxiv.org/abs/2402.05129
6. *Debate or Vote: Which Yields Better Decisions in Multi-Agent Systems?* (2025) — https://arxiv.org/abs/2508.17536
7. *Emergence of Biased Consensus in Multi-Agent LLM Debates* (2026) — https://arxiv.org/abs/2608.02827
8. Cognition, *Don't Build Multi-Agents* (2025) — https://cognition.com/blog/dont-build-multi-agents
9. Anthropic, *How we built our multi-agent research system* (2025)

此清单即本仓库的全部引用来源:principles.md 的「依据」列、README 的 Sources、示例中的推理均出自以上条目,不另引其他文献。
