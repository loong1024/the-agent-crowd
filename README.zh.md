# crowd-proof-agents

**面向多智能体 LLM 系统的独立性工程。** 一个 Claude Code skill + 一套框架无关的方法论,防止你的 agent 团队退化成乌合之众。

[English](README.md) | 简体中文

## 这是什么,为什么需要

1895 年,古斯塔夫·勒庞观察个体消融进群体之后的机制:个人判断崩溃、情绪放大、错误传染、最流利的发言者获胜。LLM agent 团队把这套机制逐条复现——而且没有人类的借口:agent 不会疲劳、不会丢面子,并且字面意义上「靠暗示驱动」。没有工程化独立性的多 agent 系统不是集成(ensemble),而是一个大脑持有自己偏见的 N 份拷贝。

这种失效在现代文献里有名字:相关误差(correlated errors)。同一个提示词、同一个模型起的 N 个 agent,是一个评审员带着 N 份自己的错误——agent 数量增加不等于准确率提高。辩论还可能更糟:agent 们收敛到一个自信的有偏共识,而不是互相纠错。解药很古老,也有据可查:Galton 1907 年的竞重人群命中答案,是因为判断彼此独立;Condorcet 陪审团定理说明独立性为何是承重假设;Surowiecki 把分水岭说得很直白——互动群体(勒庞的)vs 隔离判断的聚合。

因此本仓库的最高纲领:**判断要隔离,构建可共享(Isolate for judgment. Share for construction.)**。构建类工作(写代码、写文档)受益于共享上下文;判断类工作(评审、决策、投票)在评审者共享上下文时崩溃。这里的一切都在把这一个区分工程化。

## 七原则

| 原则 | 防止的失效 | 闻起来不对劲的信号 |
|---|---|---|
| P0 先独立,再数量 | 数 agent 总数而非独立评审数(相关误差) | 你靠增加 agent 数量指望准确率上升 |
| P1 结论隔离 | 上游结论在下游提示词里变「事实」,幻觉沿链复利 | 提示词里说「如 agent A 已确认,X 是对的」 |
| P2 编排者最后说话 | 派发者的预感锚定所有评审 | 派发词里出现「我觉得差不多了,再核一下」 |
| P3 异质优于同质 | 同模型投票相关,共享盲区永远共享 | 「三个模型一致」——其实同一个模型换了名字 |
| P4 盲审评审者 | 评审因作者 / 模型血统偏松或偏严 | 评审结论跟着作者资历走,不跟工件质量走 |
| P5 证据优于流畅 | 自信的全绿报告靠语气被信任,而非靠核查 | 一份没人能回溯到命令输出的全绿报告 |
| P6 保留异议 | 少数派异议被压成共识;异议者往往看见了 bug | 一场人人收敛、却没记录任何少数派立场的辩论 |

完整机制对照(勒庞机制 → 失效模式 → 工程对策 → 依据)见 [references/principles.md](references/principles.md)。

## 快速开始

### Claude Code

把 skill 拷进 skills 目录:

- 个人级:`~/.claude/skills/crowd-proof-agents/SKILL.md`
- 项目级:`<你的项目>/.claude/skills/crowd-proof-agents/SKILL.md`——随项目提交,队友和每个 agent 会话自动继承这套纪律。

触发场景:多 agent 设计、子 agent 派发、集成 / 辩论工作流、评审派发,或团队收敛到一个自信的错误答案时。

### 其他框架(CrewAI / LangGraph / AutoGen 等)

把 `references/` 当方法论读,零运行时依赖:

- [references/principles.md](references/principles.md) — 概念映射与文献依据
- [references/playbook.md](references/playbook.md) — 可直接粘贴进编排器提示词的派发模板、交接契约、辩论主持、合并清单
- [examples/before-after.md](examples/before-after.md) — 用于校准管线的对照案例

建议的第一步:在你下一次多 agent 派发之前,先过一遍 [SKILL.md](SKILL.md) 里的 Pre-flight 问题。

## 什么时候不要用

- 单一、界定清晰的任务:一个带好提示词的 agent 胜过协调开销。
- 构建类工作且连贯性比判断重要:保留共享上下文;不要盲目并行编辑同一批文件。
- 延迟 / 成本占主导的琐碎检查。

## 相关工作

编排「机械层」(并行波次、派活、hook)已有成熟开源方案;缺的是「判断独立性纪律」层。调研与定位见 [references/related-work.md](references/related-work.md)。

## 文献来源

1. Le Bon, *The Crowd: A Study of the Popular Mind* (1895)
2. Galton, "Vox Populi", *Nature* (1907)
3. Condorcet 陪审团定理 (1785);Surowiecki, *The Wisdom of Crowds* (2004)
4. Du et al., *Improving Factuality and Reasoning through Multiagent Debate* (2023) — https://composable-models.github.io/llm_debate
5. Smit et al., *Should We Be Going MAD? A Look at Multi-Agent Debate Strategies* (ICML 2024) — https://arxiv.org/abs/2402.05129
6. *Debate or Vote: Which Yields Better Decisions in Multi-Agent Systems?* (2025) — https://arxiv.org/abs/2508.17536
7. *Emergence of Biased Consensus in Multi-Agent LLM Debates* (2026) — https://arxiv.org/abs/2608.02827
8. Cognition, *Don't Build Multi-Agents* (2025) — https://cognition.com/blog/dont-build-multi-agents
9. Anthropic, *How we built our multi-agent research system* (2025)

## 声明

勒庞《乌合之众》(1895)是政论而非实证科学;其中「种族灵魂」等决定论已被现代科学抛弃。本仓库只借用其对群体行为的观察——去个体化、感染、暗示、对幻觉的偏好——不采纳其结论与政治立场。

## 许可

MIT,见 [LICENSE](LICENSE)。
