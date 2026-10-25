# The Agent Crowd

> **Your agent team is a crowd — unless you give it independence discipline.**
> *A Study of the Popular Mind, for your agent teams.* Named after Gustave Le Bon's *The Crowd* (1895).


<!-- EN What&why rewrite pending (DeepSeek batch): reposition as dual-source (Le Bon defense + Drucker construction) -->

## I. Why The Crowd

In 1895, Gustave Le Bon published *The Crowd: A Study of the Popular Mind*, answering a question nobody took seriously at the time: **why does a smart person turn stupid the moment they join a group?** His list of ideas became the foundation of crowd psychology:

- **Psychological unity** — individuals in a group lose their personality; their intelligence drops below the group average
- **Contagion** — emotions and conclusions spread like a virus between members; the individual cannot resist
- **Suggestion** — the group is nearly hypnotized, believing whatever it is told
- **The leader's three tools** — assertion (unproven) + repetition (a thousand times makes it true) + contagion (note: this persuasion machinery only works in a debate arena where members can see each other; isolate the intermediate drafts and its surface of operation vanishes)
- **Prestige** — a name makes people skip reason and obey directly
- **The preference for illusion** — the group does not seek truth, only fluent and confident conclusions
- **Anonymity and the disappearance of responsibility** — if nobody signs their name, nobody is accountable

Now look at your agent team: N instances of the same model, each seeing the others' intermediate drafts, no fatigue and no ego, naturally deferential in tone — **this is a purer crowd than any human group.** Every crowd pathology Le Bon described has, here, a more direct transmission path that can be cut off by engineering. Multiple agents are not inherently stronger than one: it is a coin flip between "N copies of one mind" and "a real team," and which side comes up depends on whether you have installed independence discipline.

## II. The Corresponding Agent Management Reference Patterns

| Crowd pathology | Symptom in an agent team | Management pattern |
|---|---|---|
| Psychological unity | N agents' outputs converge = N copies | **Isolate intermediate drafts** (P1): reviewers cannot see each other |
| Contagion | Upstream conclusions treated as fact downstream, compounding along the chain | **Pass artifacts, not conclusions** (P1): handoffs carry evidence/source/confidence/owner |
| Suggestion · leader assertion | The orchestrator's expectations leak into the dispatch, anchoring everyone | **The orchestrator speaks last** (P2): the dispatch contains facts only |
| Repetition + contagion | In the debate arena, the minority is crushed into consensus | **Private conclusion first, then exchange, dissent mandatory** (P6) |
| Prestige | Reviewers go easy once they know who wrote it | **Blind the reviewer** (P4): strip identity, keep the requirement, judge the artifact not the author |
| The preference for illusion | "✅ All passed" is the most contagious lie there is | **Evidence over fluency** (P5): no bare green without evidence |
| Anonymity and lost responsibility | Something breaks and nobody owns it | **Attribution + verdict level** (the Owner line of the handoff contract): conclusions trace back to a specific agent |

**The master principle (the two-domain doctrine): Isolate for judgment. Share for construction.** Sharing context while writing code is more efficient; review votes only work when reviewers are isolated from each other.

### When to activate: the four gates

| Gate | Scenario | Cost of an error |
|---|---|---|
| Acceptance gate | Batch close-out, ship / no-ship | Bug shipped to users |
| Decision gate | Finalizing a plan / merging to main / choosing a technology | Everything downstream redoes the work |
| External gate | Publishing / spending money / deleting data / outward-facing content | Irreversible |
| Trust gate | About to change direction on the strength of the agents' collective confidence | A week burned for nothing |

> **The one-line test: if this verdict is wrong, do you just rerun it, or does it burn someone else? Rerun → do not activate; burns someone else → activate.**

### Three-symptom quick check

1. Different agents' outputs are worded almost identically, and wrong in the same places.
2. All-green reports with no evidence chain.
3. Output grows more confident as it propagates, with no new evidence added.

Hit any one of these and your agent team is already becoming a mob.

## III. What's Inside

the-agent-crowd is a **Claude Code skill + a framework-agnostic multi-agent management methodology** (equally applicable to CrewAI / LangGraph / AutoGen / custom orchestration). Six pieces:

1. **SKILL.md** — the two-domain doctrine, the seven principles (P0 Independence before quantity / P1 Quarantine verdicts / P2 The orchestrator speaks last / P3 Heterogeneity over homogeneity / P4 Blind the reviewer / P5 Evidence over fluency / P6 Keep the dissent), the four gates, and seven Red Flags that your team has become a mob (the README adds the three-symptom quick check)
2. **playbook** — 5 copy-paste dispatch templates (4 judgment + 1 construction): cold-review dispatch / the Claim/Evidence/Confidence/Source/Owner handoff contract / debate moderation without shared drafts / the merge master checklist / the MBO construction dispatch
3. **Drucker reference** — organizational engineering for the construction side: MBO dispatch, federal squads, dissent-first decisions — see references/drucker.md
4. **principles** — a complete mapping of Le Bon's ideas × agent failure modes × engineering prescriptions; every prescription is grounded in LLM empirics and aggregation theory — see references/principles.md
5. **experiment protocol** — a reproducible experiment protocol covering three isolation levels + a 2×2 reviewer configuration (protocol defined, results pending)
6. **before-after cases** — a two-column comparison of the same bug (a design hypothesis; the gain awaits validation by the protocol's second experiment)

## IV. Activation

**Two install tiers (copy the whole the-agent-crowd/ directory, including SKILL.md and references/; copying only SKILL.md breaks the relative links)**
- Project-level (recommended): copy into `<project>/.claude/skills/the-agent-crowd/` and commit it with git — every session and every parallel sub-agent in that project inherits it automatically, and teammates get it on clone
- Personal-level: copy into `~/.claude/skills/the-agent-crowd/` to apply across all projects

**Three trigger modes**
- Automatic: the skill activates when a session reaches a four-gate scenario (acceptance close-out, decision and merge, external release, about to trust the agents' collective confidence); full trigger phrases in SKILL.md's description
- By name: just call `the-agent-crowd`
- Zero-trigger: the playbook templates can be copied directly and used as a dispatch-template cheat sheet

## V. When NOT to Use

- A single small task: one good prompt beats all the ceremony
- Construction-type tasks: sharing context is correct; don't parallelize edits to the same set of files
- Verdicts where the cost of a rerun ≈ zero: the one-line test already said no

## VI. 30-Second Example

Dispatching a code review —
❌ "Here's the login feature I just wrote, I looked it over and it seems fine, give it a once-over."
✅ "Cold-review the following change: `git diff main`. Against the requirement spec (attached). Every conclusion must cite file:line evidence; give each conclusion as one of the five levels: pass / fail / blocked / skipped / unverified. Do not infer or use the author's, model's, or framework's identity."

The difference isn't politeness — it's **whether the anchoring source has been cut off.**

## VII. FAQ

**Q: Will this slow down my multi-agent workflow?** The four gates guarantee that the vast majority of dispatches involve zero ceremony; gate discipline is mostly a money-saving move (isolated context = fewer tokens), and the expensive heterogeneous panel is reserved for irreversible verdicts.

**Q: Does it conflict with CrewAI/LangGraph/AutoGen?** No. It sells discipline, not code — any orchestration framework can execute these templates.

**Q: Why not just use a single agent?** In the construction domain, one strong agent with full context is often better; in the judgment domain, aggregating multiple mutually isolated reviewers is more accurate. The two-domain doctrine is the answer to this.

**Q: Why this name?** A nod to *The Crowd* — it was the first to catalog the "crowd pathologies"; and your agent team is the first group in history with the **conditions to avoid all of them completely**.

## Related Work

The full bibliography (12 entries) is in [references/related-work.md](references/related-work.md).

MIT License


---

# the-agent-crowd

> **你的 agent 军团就是一个「乌合之众」——除非你给它独立性纪律。**
> *A Study of the Popular Mind, for your agent teams.*


## 一、为什么是《乌合之众》

本体系结合两种思想设计:勒庞《乌合之众》提供防御叙事——裁决域为何必须隔离;德鲁克组织工程学提供建设叙事——构建域如何派发与组织。证据基础=LLM 实证+聚合理论;管理学处方属设计类比,待实验实测。

1895 年,勒庞出版《乌合之众:大众心理研究》(The Crowd: A Study of the Popular Mind),回答了一个当时没人认真对待的问题:**为什么一个聪明人,一进群体就变蠢?**他给出的理念清单成了群体心理学的地基:

- **心理统一律**——个体进群体,个性消失,智力降到群体平均之下
- **感染**——情绪和结论像病毒一样在成员间传播,个体不由自主
- **暗示**——群体近似被催眠,说什么信什么
- **领袖三工具**——断言(不证)+ 重复(千遍成真)+ 传染(注意:这套说服机制只在互相可见的辩论场生效;隔离中间稿即失作用面)
- **威望**——名头让人跳过理性直接服从
- **渴求幻象**——群体不追求真理,只追求流畅自信的结论
- **匿名与责任消失**——没人署名,就没人负责

现在看你的 agent 军团:同一个模型的 N 个实例、互相看得见中间稿、没有疲劳没有面子、天生顺从语气——**这是一个比任何人类群体都更纯粹的群体**。勒庞笔下的每种群体病,在这里都有一条更直接、且可被工程切断的传染路径。多 agent 不是天然强于单体:它是「一个头脑的 N 份复印件」与「真正的军团」之间的一次掷硬币,掷出哪面,取决于你有没有装独立性纪律。

## 二、对应的 agent 管理参考模式

| 乌合之众的病 | agent 军团里的症状 | 管理模式 |
|---|---|---|
| 心理统一律 | N 个 agent 输出趋同 = N 份复印件 | **隔离中间稿**(P1):评审互不可见 |
| 感染 | 上游结论被下游当事实,沿链复利 | **传工件不传结论**(P1):交接带证据/出处/置信/署名 |
| 暗示·领袖断言 | 编排者预期写进派发词,全体被锚定 | **主持人最后亮牌**(P2):派发词只含事实 |
| 重复+传染 | 辩论场里少数派被碾成共识 | **先私下结论、再交换、必引异议**(P6) |
| 威望 | 评审知道作者是谁就放水 | **盲审**(P4):剥身份、留需求,判工件不判来头 |
| 渴求幻象 | 「✅全部通过」是最具传染力的谎言 | **证据优于流畅**(P5):禁止无证据裸绿 |
| 匿名责任消失 | 出错没人背锅 | **署名+判级**(P1 契约 Owner 行):结论追责到具体 agent |

**总纲(两域论):裁决要隔离,构建可共享。** 写代码共享上下文更高效;评审投票必须互相隔离才有效。

### 什么时候启用:四个闸门

| 闸门 | 场景 | 错误代价 |
|---|---|---|
| 验收闸 | 批次收官 ship / no-ship | bug 发给用户 |
| 拍板闸 | 方案定稿 / 合并 main / 选型 | 下游全部返工 |
| 对外闸 | 发布 / 花钱 / 删数据 / 对外内容 | 不可挽回 |
| 信任闸 | 准备照 agent 集体自信结论改方向 | 白烧一周 |

> **判断口诀:这个裁决错了,是重跑一次就完,还是烧到别人?重跑 → 不启用;烧到别人 → 启用。**

### 三症状速查

1. 不同 agent 输出措辞高度雷同,且错在相同处。
2. 全绿报告、无证据链。
3. 输出越传越自信,却没有新增证据。

命中任意一条,你的 agent 军团已在乌合之众化。

## 三、skill 整体介绍

the-agent-crowd 是一个 **Claude Code skill + 框架无关的多 agent 管理方法论**(CrewAI / LangGraph / AutoGen / 自研编排同样适用)。六件内容:

1. **SKILL.md**——两域论纲领、七原则(P0 独立性先于数量 / P1 结论隔离 / P2 编排者最后说话 / P3 异质优于同质 / P4 盲审 / P5 证据优于流畅 / P6 保留异议)、四闸门、七条「军团已乌合之众化」信号(Red Flags,README 另附三症状速查)
2. **playbook**——5 个可复制粘贴的派发词模板(4 判断 + 1 构建):冷审派发 / 五行交接契约 / 断稿辩论主持 / 合并五问 / MBO 构建派发
3. **德鲁克参考**——建设侧的组织工程学:MBO 派发、联邦编队、异议先行决策,详见 references/drucker.md
4. **principles**——勒庞理念 × agent 失效模式 × 工程处方完整对照,处方依据一律挂 LLM 实证与聚合理论,详见 references/principles.md
5. **experiment protocol**——三档隔离度 + 评审配置 2×2 的可复现实验协议(协议已定义,结果待跑)
6. **before-after 案例**——同一个 bug 的两栏对照(设计假设,增益待协议第二实验验证)

## 四、启用方式

**安装两档(拷入整个 the-agent-crowd/ 目录,含 SKILL.md 与 references/,单拷 SKILL.md 会断开相对链接)**
- 项目级(推荐):拷入 `<项目>/.claude/skills/the-agent-crowd/`,随 git 提交——该项目每个会话、每个并行子 agent 自动继承,队友 clone 即得
- 个人级:拷入 `~/.claude/skills/the-agent-crowd/`,全项目生效

**触发三式**
- 自动:会话进入四闸门场景(验收收官、拍板与合并、对外发布、准备信任 agent 集体自信结论)时进场,完整触发词见 SKILL.md description
- 点名:直接叫 `the-agent-crowd`
- 零触发:playbook 模板可直接抄,当派发词抄写板用

## 五、什么时候不要用

- 单个小任务:一个好 prompt 胜过全部仪式
- 构建型任务:共享上下文是对的,别乱并行改同一批文件
- 重跑成本≈零的裁决:口诀说了,不启用

## 六、30 秒上手示例

派代码冷审——
❌ 「这是刚写的登录功能,我看了基本没问题,你把把关」
✅ 「冷审以下改动:`git diff main`。对照需求 spec(附上)。每条结论附 file:line 证据;结论按 pass/fail/blocked/skipped/unverified 五级给出。不要推断或使用作者、模型、框架身份。」

差别不在客气与否,在**锚定源有没有被掐掉**。

## 七、FAQ

**Q:会不会拖慢我的多 agent 流程?** 四闸门保证绝大多数派发零仪式;闸口纪律多数是省钱操作(隔离上下文 = 更少 token),贵的异构面板只留给不可逆裁决。

**Q:和 CrewAI/LangGraph/AutoGen 冲突吗?** 不冲突。它只卖纪律不卖代码,任何编排框架都能执行这些模板。

**Q:为什么不干脆只用一个 agent?** 构建域,一个带完整上下文的强 agent 常常更好;裁决域,多个互相隔离的评委聚合才更准。两域论就是回答这个的。

**Q:为什么叫这个名字?** 向《乌合之众》致意——它第一个把「群体病」清单化;而你的 agent 军团,是史上第一个**有条件完全避免这些病**的群体。

## 相关工作

完整文献清单(12 条)见 [references/related-work.md](references/related-work.md)。

MIT License
