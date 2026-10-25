# the-agent-crowd

> 命名源自勒庞《乌合之众》(*The Crowd: A Study of the Popular Mind*, 1895)——一份写给 agent 军团的「大众心理研究」。

**面向多智能体 LLM 系统的独立性工程。** 一个 Claude Code skill + 一套框架无关的方法论,防止你的 agent 团队退化成乌合之众。

[English](README.md) | 简体中文

## 什么时候启用:四道闸门

本 skill 只存在于四个闸门——裁决一旦错了,烧掉的不是一次重跑:

| 闸门 | 时刻 | 错的代价 |
|---|---|---|
| 验收闸 | 批次收官 ship / no-ship | 错报绿灯 = bug 发给用户 |
| 拍板闸 | 方案定稿、合并 main、架构选型 | 错拍板 = 下游全返工 |
| 对外闸 | 公开发布、花钱、删数据、对外内容 | 错了追不回 |
| 信任闸 | 准备照 agent 集体自信结论改变方向 | 错信任 = 白烧一周 |

**判断口诀:这个裁决错了,是重跑一次就完,还是烧到别人?重跑→本 skill 不启用;烧到别人→继续读。**

闸门内按 claim 风险分级:重跑成本低的小管线用轻量契约(口头置信 + 抽查);五行契约与全套面板只留给烧到别人的裁决。

## 三症状快速自检

1. 不同 agent 的输出措辞高度雷同。
2. 全绿报告、无证据链。
3. 语言风格同质化。

命中任意一条,你的 agent 军团已在乌合之众化。

## 这是什么,为什么需要

名字借自古斯塔夫·勒庞《乌合之众》(1895):他笔下的群体病症——个人判断崩溃、情绪放大、错误传染、最流利的发言者获胜——在多 agent 体系里确有对应物。但本仓库的工程处方不从勒庞推导:真实依据是 LLM 实证(谄媚、锚定、相关误差、上下文污染)+ 现代聚合理论(Galton 1907;Condorcet 1785;Surowiecki 2004)。勒庞对人类群体的机制主张已被现代研究修正(McPhail 1991;Postmes & Spears 1998)——我们只借失效叙事,不采纳其机制、结论与政治立场。

这种失效在现代文献里有名字:相关误差(correlated errors)。同一个提示词、同一个模型起的 N 个 agent,是一个评审员带着 N 份自己的错误——agent 数量增加不等于准确率提高。辩论还可能更糟:agent 们收敛到一个自信的有偏共识,而不是互相纠错。有据可查的解药是对独立判断做聚合:Galton 1907 年的竞重人群命中答案,是因为判断彼此独立;Condorcet 陪审团定理说明独立性为何是承重假设;Surowiecki 把分水岭说得很直白——独立性区分了乌合之众与群体智慧。

因此有了两域论:**判断要隔离,构建可共享(Isolate for judgment. Share for construction.)**。构建类工作(写代码、写文档)受益于共享上下文;判断类工作(评审、决策、投票)在评审者共享上下文时崩溃。这里的一切都在把这一个区分工程化——而且只在上面四道闸门处生效;其余时刻,全速跑。

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

- 个人级:`~/.claude/skills/the-agent-crowd/SKILL.md`
- 项目级:`<你的项目>/.claude/skills/the-agent-crowd/SKILL.md`——随项目提交,队友和每个 agent 会话自动继承这套纪律。

触发场景:验收收官、拍板与合并、对外发布,以及准备信任 agent 集体自信结论的时刻;或团队收敛到一个自信的错误答案时。

### 其他框架(CrewAI / LangGraph / AutoGen 等)

把 `references/` 当方法论读,零运行时依赖:

- [references/principles.md](references/principles.md) — 概念映射与文献依据
- [references/playbook.md](references/playbook.md) — 可直接粘贴进编排器提示词的派发模板、交接契约、辩论主持、合并清单
- [experiments/protocol.md](experiments/protocol.md) — 最小复现协议:验证或证伪本仓库的机制主张(协议已定义,结果待跑)
- [examples/before-after.md](examples/before-after.md) — 用于校准管线的对照案例

建议的第一步:在你下一次闸门派发之前,先过一遍 [SKILL.md](SKILL.md) 里的 Pre-flight 问题。

## 什么时候不要用

本 skill 只在四个闸门存在。其余时刻:全速并行、共享上下文、零仪式。构建类工作带着共享上下文胜过 N 个互相隔离的构建者(Cognition 2025);延迟 / 成本占主导的琐碎检查根本不需要闸门。

## 相关工作

编排「机械层」(并行波次、派活、hook)已有成熟开源方案;缺的是「判断独立性纪律」层。调研与定位见 [references/related-work.md](references/related-work.md)。

## 文献来源

1. Le Bon, *The Crowd: A Study of the Popular Mind* (1895)
2. Galton, "Vox Populi", *Nature* (1907)
3. Condorcet 陪审团定理 (1785);Surowiecki, *The Wisdom of Crowds* (2004)
4. Du et al., *Improving Factuality and Reasoning through Multiagent Debate* (2023) — arXiv 2305.14325,https://arxiv.org/abs/2305.14325;落地页:https://composable-models.github.io/llm_debate
5. Smit et al., *Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs* (ICML 2024) — https://arxiv.org/abs/2311.17371
6. *Debate or Vote: Which Yields Better Decisions in Multi-Agent Systems?* (2025) — https://arxiv.org/abs/2508.17536
7. *Emergence of Biased Consensus in Multi-Agent LLM Debates* (2026) — https://arxiv.org/abs/2608.02827
8. Cognition, *Don't Build Multi-Agents* (2025) — https://cognition.com/blog/dont-build-multi-agents
9. Anthropic, *How we built our multi-agent research system* (2025)
10. Sharma et al., *Towards Understanding Sycophancy in Language Models* (2023) — arXiv 2310.13548,https://arxiv.org/abs/2310.13548
11. Chan et al., *ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate* (ICLR 2024) — arXiv 2308.07201,https://arxiv.org/abs/2308.07201
12. McPhail, *The Myth of the Madding Crowd* (1991);Postmes & Spears,去个体化元分析,*Psychological Bulletin* (1998)

## 声明

勒庞《乌合之众》(1895)是政论而非实证科学;其中「种族灵魂」等决定论已被现代科学抛弃——最直接的反证见 McPhail(1991)与 Postmes & Spears(1998,*Psychological Bulletin*)的去个体化元分析。本仓库只借用其对群体行为的观察——去个体化、感染、暗示、对幻觉的偏好——作为命名隐喻与失效叙事;工程处方的依据是 LLM 实证与聚合理论,不采纳勒庞的结论与政治立场。

## 许可

MIT,见 [LICENSE](LICENSE)。
