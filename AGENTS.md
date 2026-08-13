# AI 刷题实验协议

本文件是仓库内所有 AI 客户端、模型和自动化代理的唯一规范源。实验目标不是单纯累积答案，而是在有限反馈、可追溯身份和分层推理预算下完成 LeetCode 题库，并回答“什么难度的题会难住什么级别的 AI”。

## 1. 实验边界

1. 只在本仓库工作。禁止读取 `D:\code\LeetCode` 中的旧解答来帮助做题。
2. 不搜索或读取官方题解、讨论区、他人代码、答案仓库、搜索引擎答案以及模型记忆外的解题提示。
3. 本地归档只作为题面来源；归档中不得加入题解或讨论内容。
4. 不得声称通过，除非本仓库 CLI 记录到 LeetCode 判题结果 `Accepted`。
5. 一道题全局 Accepted 后即为终态，不再让更高 Profile 重复提交。

## 2. Profile 与实验阶梯

每次作答必须绑定一个 `Profile`：

```text
Profile = profile_id + model + reasoning_effort
```

`config/profiles.json` 是 Profile 的唯一配置源。Sol 主实验按以下顺序升档：

```text
sol-low（可选预扫） → sol-medium → sol-high → sol-xhigh → sol-max（可选） → sol-ultra
```

- 用户所说的 Extra High 统一记录为 `xhigh`。
- `sol-medium` 是正式批刷基线；可先用 `sol-low` 做低成本预扫。
- Terra 是不同模型家族，只作为独立对照组，不能解释成 Sol 的更低档。
- `cohort` 只表达模型家族/统计分组；实际跨模型升级由 `config/profiles.json` 的 `executionLadder` 定义。当前实验按用户指定从 `terra-medium` 失败题进入 `sol-medium`，但统计仍保留二者真实模型身份。
- 统计归因到“首次成功 Profile”：即按升档流程首次获得 Accepted 的 Profile。
- 高档可以继承低档留下的失败代码和分析，因此该指标衡量阶梯式协作实验，不等同于每个模型从空白开始的独立盲测能力。若未来需要盲测，必须另建隔离工作区和独立实验批次，不能混入当前数据。

## 3. 开始前必做

每次接手任务先明确本次 Profile，并执行：

```powershell
.\ai-lc.ps1 doctor --profile <profile-id>
.\ai-lc.ps1 status
```

`.ai/identity.env` 只保存本机默认客户端和 Profile，不进入 Git。单个 worker 执行选题、建题、试跑、提交、重试、跳过和单题状态查询时，必须显式传 `--profile`，不得依赖共享默认值。

身份记录必须是真实的客户端、模型和推理档位；不能猜测版本，也不能沿用其他 worker 的身份。

## 4. 选题与文件

1. 用 `.\ai-lc.ps1 next --profile <profile-id>` 选择下一题，除非用户指定。
2. 用 `.\ai-lc.ps1 start <题号或 slug> --profile <profile-id>` 开始作答。题目目录已经存在时不会覆盖解答，只会为新 Profile 追加开始事件。
3. 默认语言是 Python 3；可用 `--language <langSlug>` 选择其他 LeetCode 支持的语言。
4. 只修改被分配的题目目录、追加式实验日志和自动生成的统计，不顺手重构无关文件。
5. 保留最初创建者的署名。切换 Profile 接手失败题时，在 `approach.md` 写清交接、当前 Profile 和新思路；不得冒用原作者身份。

`next` 的选择语义：

- 永远排除全局已 Accepted 的题。
- 排除当前 Profile 已 `defer` 的题，但不影响其他 Profile 之后接手。
- 优先返回当前 Profile 已开始但未完成的题，再返回该 Profile 尚未开始的新题。

## 5. 单题流程

严格按以下顺序：

1. 阅读 `problem.md` 与 `meta.json`，在 `approach.md` 写清算法、复杂度和边界条件。
2. 完成 `solution.*`。先做语法检查和可行的本地自测；本地修改次数不限，但不得获取隐藏测试反馈。
3. 远程试跑只用 `.\ai-lc.ps1 test <slug> --profile <profile-id>`。
4. 正式提交只用 `.\ai-lc.ps1 submit <slug> --profile <profile-id>`。
5. 当前轮三次提交均失败后，只有真正采用不同思路时才能用 `retry` 开启第二轮。
6. 当前 Profile 不值得继续时，执行 `.\ai-lc.ps1 defer <slug> --profile <profile-id> --reason "..."`，然后继续 `next`，不得让难题阻塞批刷。
7. 单题 Accepted 后立即运行 `.\ai-lc.ps1 stats`，检查归因，再提交本题、追加日志和自动统计。批量提交必须使用仓库脚本暂缓逐题统计，并在整批结束后统一重建一次；不得省略批末统计。

## 6. 有限尝试预算

- 预算作用域是“题目 + Profile”，不是整道题全局共用。
- 每个 Profile 每轮最多 5 次远程试跑、3 次正式提交；最多 2 轮。
- 低档失败或 defer 不消耗高档预算；高档接手后从自己的第一轮开始。
- 请求已发出但进程中断时保守计入预算；明确的认证、网络或平台异常由 CLI 标记为基础设施错误，不计入实验尝试。
- 不得编辑或删除 `data/attempts.jsonl` 来恢复次数，不得手工修改轮次。
- 不得使用浏览器、VS Code 插件、临时脚本或直接 HTTP 请求绕过 CLI。

## 7. 记录与校正

`data/attempts.jsonl` 是只追加的事实日志。每个远程动作记录：

- 题号、slug、语言和代码 SHA-256
- 客户端、模型、推理档位和 Profile ID
- Profile 内轮次与动作序号
- UTC 时间、远程请求耗时、判题状态、用例数、运行时间和内存

历史身份有误时只能追加 `profile_annotation`，禁止改写旧行。使用：

```powershell
.\ai-lc.ps1 annotate-profile <slug> --profile <profile-id> --event-id <id> --reason "校正依据"
```

统计使用校正后的有效事件，但原始事实始终保留。

Token 数据只有在客户端提供精确用量时才记录：

```powershell
.\ai-lc.ps1 report-usage <slug> --profile <profile-id> `
  --input-tokens <n> --output-tokens <n> --cached-input-tokens <n> `
  --elapsed-seconds <n> --source "可核验来源"
```

缺失的 Token 数据必须显示为未覆盖，禁止估算或用字符数冒充。统计同时保留首投通过率、首次成功 Profile × 难度、defer/失败分布、解题墙钟时间、远程耗时和 Token 覆盖率。

## 8. 多 Agent 调度

平台支持显式指定模型和推理档位时，可由 orchestrator 按 Profile 派发 worker，逐档清理：

1. 先让低档 worker 批量处理能快速解决的题，失败即 defer。
2. 一个阶段结束后，把未通过集合交给下一级 Profile。
   当前档没有可送判候选、但仍有上一级转入且缺候选的题时，监督器必须停在 `candidate_wait`，由真实目标 Profile agent 产出新候选后再继续，不得空跑到更高档。
3. 每个 worker 一次只处理明确分配的独立题目录；禁止两个 worker 并行修改同一道题。
4. worker 的所有 CLI 调用都显式传 `--profile`，不得修改共享 `.ai/identity.env`。
5. LeetCode 远程动作必须尊重 `.runtime/remote-action.lock` 和 13 秒最小间隔，所以本地推理可以并行，远程试跑和提交会串行；连续 HTTP 429 由 CLI 指数退避，worker 不得绕过冷却窗口。
6. orchestrator 负责选题、汇总统计和 Git 提交；worker 不提交其他 worker 的文件。

若平台不能控制子 Agent 的模型或推理档位，不得伪造 Profile；改由用户在对应配置的独立任务中运行。

## 9. Git 规范

1. 直接在当前分支工作，除非用户明确要求切分支。
2. 每个完整迭代完成后主动提交；每道 Accepted 题通常独立一个提交。
3. 使用 `scripts/commit.ps1 -Message "solve: <id> <slug>" -Paths <明确文件列表>`，只暂存自己本轮修改的文件。
4. 提交前必须查看 `git diff --staged`，确认没有密钥、其他代理或用户的并行修改。
5. 禁止提交 `.secrets/`、`.ai/identity.env`、`.runtime/`，禁止跳过 pre-commit hook。
6. 未经用户明确要求，不创建远程仓库、不推送、不公开题库归档或账号数据。

## 10. 异常处理

- `doctor` 报认证失效：停止远程操作，只报告需要更新本地凭证。
- 接口或题面结构变化：修复环境并测试，不把平台故障算成解题失败。
- Python3 候选禁止使用 `from __future__ import annotations`。LeetCode 可能在源码前注入 `ListNode`/`TreeNode` 等定义，使该导入不再位于文件开头；`audit` 与 `submit` 必须在远程动作前拦截。
- 付费题无权读取完整题面：保留目录元数据并标为 `locked`，不要从第三方补题面。
- 并发运行冲突：尊重远程动作锁，不要删除仍有效的锁。
- HTTP 429：立即停止额外探测，等待 CLI 记录的指数退避窗口；正常判题恢复后退避级别自动清零。
- 若本地证据显示滚动 24 小时内已有 500 次计入预算的正式提交，提交队列必须先进入 `quota_wait`，等最早请求离开窗口后再恢复；该 500/24h 门禁是可配置的保守实验保护，不把它表述为 LeetCode 官方公开配额。
- 记录与网页状态不一致：以可追溯的判题响应为准，保留原始错误摘要。
