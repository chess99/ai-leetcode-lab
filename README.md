# AI LeetCode Lab

这是一个供不同 AI 客户端共同使用的 LeetCode 分层刷题实验仓库。它已经归档题库、脚本化试跑和提交，并以追加日志记录“哪一个模型与推理档位首次解决了哪一道题”。

仓库与旧目录 `D:\code\LeetCode` 完全隔离。旧答案、官方题解、讨论区和搜索结果都不进入实验。

## 实验方法

一次实验身份由 `Profile ID + 模型 + 推理档位` 组成。主阶梯配置在 `config/profiles.json`：

```text
sol-low（可选） → sol-medium → sol-high → sol-xhigh → sol-max（可选） → sol-ultra
```

Profile 的 `cohort` 表示模型家族/统计分组，`executionLadder` 则表示本次实验真实升级顺序。当前执行顺序是 `terra-medium → sol-medium → sol-high → sol-xhigh → sol-ultra`：Terra 仍是不同模型家族的对照基线，但它未通过的题会按用户指定实验流程交给 Sol。某题在当前 Profile 不值得继续时可以 `defer`，它会从当前档位的选题队列中移除，并在下一执行档获得完整尝试预算。

最终统计的是“首次成功 Profile”。这是逐级升级、允许高档继承低档失败产物的实验结果，不是每个模型从空白开始的独立盲测结果。

## 已搭好的能力

- 归档 4,406 道题的目录、题面和代码模板；免费题与付费锁定题分开统计。
- 直接调用 `leetcode.cn` 接口，脚本化远程试跑、正式提交和判题轮询。
- 按“题目 + Profile”限制尝试：每轮 5 次试跑、3 次提交、最多 2 轮。
- 当前档位 defer 后继续刷其他题，后续 Profile 可重新接手。
- 追加式事实日志和无损历史校正，不通过改日志恢复预算。
- 统计首次成功 Profile × 难度、首投通过率、失败/defer、墙钟时间、远程耗时和 Token 覆盖率；`stats/summary.json` 的 `capabilityByDifficulty.byProblem` 保存覆盖全部免费题的逐题能力归属，可从矩阵下钻复核。
- 只有客户端提供精确 Token 数据时才记录；缺失值不会估算。
- 多 worker 可并行推理不同题，远程动作通过共享锁串行化。
- 连续 HTTP 429 使用 60 秒起步、最高 15 分钟的指数退避；任一正常判题响应会重置退避级别。另有可配置的滚动 24 小时 / 500 次正式提交保护门禁，避免已观察到额度耗尽形态时反复探测；这是本实验的保守策略，不宣称为平台官方公开配额。
- Git 提交前扫描 LeetCode 会话和常见密钥格式。

## 快速开始

初始化和检查：

```powershell
.\scripts\bootstrap.ps1
.\ai-lc.ps1 profiles
.\ai-lc.ps1 doctor --profile sol-medium
.\ai-lc.ps1 stats
```

处理一道题：

```powershell
.\ai-lc.ps1 next --profile sol-medium --difficulty easy
.\ai-lc.ps1 start <slug> --profile sol-medium
# 编辑 problems/<题号-slug>/solution.py 与 approach.md
.\ai-lc.ps1 candidate-ready <slug> --profile sol-medium `
  --level oracle --validation "题面样例与随机小规模 oracle 对拍通过"
.\ai-lc.ps1 test <slug> --profile sol-medium
.\ai-lc.ps1 submit <slug> --profile sol-medium
.\ai-lc.ps1 stats
```

当前档位跳过，不阻塞队列：

```powershell
.\ai-lc.ps1 defer <slug> --profile sol-medium --reason "当前思路无法在有限反馈内定位错误"
.\ai-lc.ps1 next --profile sol-medium
```

批量候选都完成本地验证后，可启动可恢复的串行送判队列：

```powershell
.\scripts\run-submit-queue.ps1 -Profile terra-medium
```

完整 Profile 阶梯可以交给监督器依次送判：

```powershell
.\scripts\run-profile-ladder.ps1
```

队列始终通过仓库 CLI 提交，并只选择“当前 Profile 的 candidate-ready 哈希与工作区代码一致”的题；选择器和提交器均执行此门禁。监督器从 `executionLadder` 读取真实顺序。队列遵守共享锁、13 秒最小间隔、滚动提交额度门禁和指数退避。一次正常判题失败会把该题 defer 给下一 Profile；如果下一档仍缺真实模型产出的新候选，队列进入 `candidate_wait`，不会误跳过该档。HTTP 429、网络和平台故障不计模型失败。运行状态保存在忽略目录 `.runtime/submit-queue-state.json`；创建 `.runtime/submit-queue.stop` 可在当前动作结束后安全停止。`-MaxTerminalResults` 可用于小批量试运行，`-StatsEvery` 控制统计刷新频率；`ai-lc.ps1 quota-status` 可查看本地证据计算出的窗口占用和下次允许时间。

更高档位接手同一题时，`start` 不会覆盖现有解答：

```powershell
.\ai-lc.ps1 start <slug> --profile sol-high
.\ai-lc.ps1 status <slug> --profile sol-high
```

如果某题先 defer，后来又在同一 Profile 得到可靠候选，必须用追加事件恢复：

```powershell
.\ai-lc.ps1 candidate-ready <slug> --profile sol-high `
  --level oracle --validation "新的算法通过小规模 oracle"
.\ai-lc.ps1 resume <slug> --profile sol-high --reason "已有可靠候选，恢复送判"
```

若客户端能给出精确用量，可单独追加；不能获取时不要调用：

```powershell
.\ai-lc.ps1 report-usage <slug> --profile sol-medium `
  --input-tokens 123 --output-tokens 45 --cached-input-tokens 67 `
  --elapsed-seconds 8.5 --source "客户端 usage API"
```

## 目录结构

```text
ai-leetcode-lab/
├─ AGENTS.md                 # 所有 AI 的唯一实验协议源
├─ CLAUDE.md                 # 指向 AGENTS.md 的兼容入口
├─ config/
│  ├─ experiment.json       # 尝试预算和同步参数
│  └─ profiles.json         # 模型、推理档位和实验阶梯
├─ ai_leetcode/              # 无第三方依赖的 CLI 实现
├─ archive/
│  ├─ catalog.json           # 全量题目元数据
│  └─ problems/              # 题面和模板原始归档
├─ problems/                 # 开始作答后生成的每题工作目录
├─ data/attempts.jsonl       # 只追加的事实事件
├─ stats/                    # 自动生成的汇总
├─ skills/                   # 项目级通用 skill 唯一来源
├─ .ai/identity.env          # 本机默认客户端/Profile，不入 Git
└─ .secrets/leetcode.env     # 专用账号凭证，不入 Git
```

Claude、Codex、通用 Agents 和 CatPaw 的兼容 skill 入口均指向根目录 `skills/`，实验规范统一来自根目录 `AGENTS.md`。

## 身份与数据解释

`.ai/identity.env` 仅提供单人交互时的默认值。自动化 worker 必须在每次命令中显式传 `--profile`，防止并发任务互相覆盖身份。

高档首次通过说明“该题在既定升档流程中直到此档才通过”，但不能直接推出低档模型在全新上下文中永远无法解决。若要比较纯模型能力，应另建独立盲测 cohort，不能复用当前失败代码。

## 凭证安全

只保存 `csrftoken` 与 `LEETCODE_SESSION`，不保存浏览器统计、广告或设备 Cookie。`.secrets/` 已被 Git 忽略，pre-commit hook 会继续扫描暂存内容。

由于凭证曾经通过聊天传递，环境稳定后建议重新登录 LeetCode 并更新本地文件，使旧会话失效。
