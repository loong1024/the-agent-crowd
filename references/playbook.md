# Playbook:可复制粘贴的派发模板与反模式表

配合 SKILL.md 的七原则使用。四个模板覆盖多 agent 判断管线的四个环节:派发(A)、交接(B)、辩论(C)、合并(D)。占位符用 `<尖括号>` 标出,替换后即可粘贴使用。模板正文用英文(多数 LLM 通道对英文指令最稳),说明用中文。

## Template A — 冷审派发(Cold Review Dispatch)

对应 P0 / P2 / P4 / P5:零上下文、盲审、证据强制、分级结论、不透露派发者倾向。

```text
You are an independent reviewer. You have no prior context on this work, and that is deliberate.

Task: Review <artifact-path> against <spec-or-requirement>.
Scope: <exact scope>. Nothing outside this scope is in scope.

Rules:
1. Judge the artifact only. Any author, model, or framework identity you think you can infer is NOT part of your input — ignore it.
2. Every finding must carry evidence: a file:line reference, a command output, or a metric. No evidence, no finding.
3. Do not assume anything works that you have not seen run. To verify behavior, run: <commands-to-run>
4. You are not told what the dispatcher expects. Do not try to satisfy an expectation — check the artifact against the spec.

Output format (mandatory):
- Verdict: one of pass | fail | blocked | skipped | unverified
- Findings: [{severity, claim, evidence, suggested_fix}, ...]
- Evidence trail: map every claim to its command output or file:line
- Anything you could not verify: mark it unverified. Do not guess.
```

要点:
- 不得包含任何作者 / 模型身份信息(P4);
- 不得包含编排者自己的预期或倾向词(P2);
- 结论六选一堵死裸绿:pass / fail 之外,blocked=环境问题无法审,skipped=主动跳过的范围,unverified=审了但证据不足,不许猜(P5)。

## Template B — 交接契约(Handoff Contract)

对应 P1 / P3 / P6:任何 agent 之间的结论传递必须套这个五行块;没有 Evidence 的 Claim 自动降级 unverified,下游不得当作事实使用。

```text
Claim:      <one-sentence assertion>
Evidence:   <command output | file:line | metric — something a third party can re-run to confirm>
Confidence: high | medium | low
Source:     <which agent produced this, from which artifact>
Owner:      <named agent accountable for this claim — audit and escalation go here>
```

要点:
- Evidence 为空时,该 Claim 必须标记为 `unverified`;
- Source 必填:合并者靠它识别同源双票(P3);
- Owner(署名)必填:结论可追责到具体 agent——这是对去个体化 / 责任稀释的直接处方(P6);
- 下游收到后应抽查 Evidence,而不是原样转发 Claim(P5)。

## Template C — 辩论主持(Debate Moderation)

对应 P3 / P6:三阶段辩论——先各自私下结论、结构化交换、再各自私下终票;合并时必须引用异议。

```text
This is a moderated debate with N agents. Follow the phases strictly.

Governance (apply before Phase 1):
- Every agent writes its verdict PRIVATELY and submits it before the exchange phase opens. A verdict written after seeing others' drafts is invalid.
- Speaking order in every exchange round is randomized (draw lots); no agent may open or close a round by default.

Phase 1 — Private verdicts
Each agent writes its own conclusion and evidence WITHOUT seeing any other agent's output. Submit before any exchange happens.

Phase 2 — Structured exchange
Agents exchange ARGUMENTS ONLY — never verdicts, never confidence levels. Required format:
  "My strongest argument for/against X is ..., supported by <evidence>."

Phase 3 — Private final votes
Each agent re-answers independently, without seeing others' final answers. A changed vote must cite which argument changed it.

Merge rule
The merged report must quote every dissenting position verbatim and state why it was overruled (or why it wins). A convergence with no recorded minority position is an INVALID merge.
```

要点:
- Governance 两句治理细节源自勒庞对议会式群体议事的描述:群体议事若无固定程序,先发言者与雄辩者就接管全场;写票在先、抽签定序,正是把「程序」本身当作锚定的对策;
- Phase 1 是 Condorcet 条件的直接落地:独立作答;
- Phase 2 只交换论证、不交换结论倾向,压低感染与威望效应;
- Phase 3 保留辩论的价值、隔离锚定;「必引异议」把少数派写进制度。

## Template D — 合并清单(Merge Checklist)

对应 P0 / P1 / P2 / P5 / P6:合并者(通常是编排者)在发布合并结论前的五问。

```text
Before publishing the merged verdict, answer all five questions:

1. Bare green?  Every pass must trace to a command output or file:line. Any bare green invalidates the merge.
2. Dissent quoted?  Every minority position must be quoted, with an explicit overrule-or-adopt reason.
3. Unsourced conclusions?  Any claim without a Source line goes back to its producer for evidence.
4. Same-source double votes?  Agents sharing a model or a materially identical prompt count as ONE vote. Recount.
5. Verdict after collection?  The orchestrator's own opinion may only be disclosed after all independent verdicts were collected. If it leaked earlier, re-dispatch.

If any answer fails, the merge is invalid: fix it, then re-run this checklist.
```

## 反模式表(与 SKILL.md 的 Red Flags 一一对应)

| # | 症状 | 病因 | 处方 |
|---|---|---|---|
| 1 | 不同 agent 的输出措辞近乎相同 | 同提示词同模型:一个评审的 N 份拷贝,错误相关(Red Flag 1) | P0+P3:数独立评审;换模型通道或实质性改写提示词;同源票只记一票 |
| 2 | 一致性来得快得可疑 | 派发词泄露了编排者预期,评审在附和而非判断(Red Flag 2) | P2+Template A:派发词只含任务事实;编排者意见收齐结论后再披露 |
| 3 | 全绿报告、无证据链 | 断言—重复—传染:下游信语气不信核查(Red Flag 3) | P5+Template A/D:每条 pass 回溯到命令输出或 file:line;裸绿按无效合并处理 |
| 4 | 评审质量跟着作者走,不跟工件走 | 威望效应:身份信息使评审系统性偏松或偏严(Red Flag 4) | P4+Template A:剥离作者、模型与历史结论后再派发 |
| 5 | 辩论结论漂向最先或最大声的发言者 | 感染+威望:先发言者锚定全场(Red Flag 5) | P6+Template C:先私下结论,只交换论证不交换倾向,终票私下重收 |
| 6 | 一个错误穿过 N 层评审仍存活 | 各层共享同一盲区——同一处错复制了 N 份(Red Flag 6) | P3:关键层换不同模型通道复评;用 Template A 冷审取代层层互审 |
| 7 | 报告每经过一跳就更自信 | 裸结论被当作事实传递,置信度沿链虚增(Red Flag 7) | P1+Template B:交接契约强制 Evidence;无 Evidence 的 Claim 降级 unverified |
