# AI LeetCode Lab

这是一个供不同 AI 客户端共同使用的 LeetCode 刷题实验仓库。重点不是“把答案攒下来”，而是可重复地观察 AI 在有限反馈下能独立解决多少算法题、失败在哪里、重试是否真的带来改进。

仓库与旧目录 `D:\code\LeetCode` 完全隔离。旧目录只用于确认历史环境，不作为解题资料；题解、讨论区和旧答案都不进入本实验。

## 已搭好的能力

- 直接调用 `leetcode.cn` 当前接口，不依赖 VS Code 插件或网页操作。
- 同步完整题目目录，可断点归档题面与各语言代码模板。
- 从归档创建规范的本地题目目录，并自动写入 AI 客户端/模型署名。
- 脚本化远程试跑、正式提交和判题轮询。
- 强制有限尝试：每轮 5 次远程试跑、3 次正式提交，最多 2 轮。
- 追加式实验日志，记录身份、轮次、代码哈希、结果、运行时间和内存。
- 生成 Markdown/JSON 统计，便于复盘首投通过率、总通过率和失败分布。
- Git 提交前密钥扫描，密钥文件和运行锁均被忽略。

## 快速开始

PowerShell：

```powershell
.\scripts\bootstrap.ps1
.\ai-lc.ps1 doctor
.\ai-lc.ps1 sync
.\ai-lc.ps1 sync --with-content
```

未来开始刷题时：

```powershell
.\ai-lc.ps1 next
.\ai-lc.ps1 start two-sum
# 编辑 problems/0001-two-sum/solution.py
.\ai-lc.ps1 test two-sum
.\ai-lc.ps1 submit two-sum
.\ai-lc.ps1 stats
```

第二轮只有在本轮 3 次提交全部失败后才能开启：

```powershell
.\ai-lc.ps1 retry two-sum --reason "改用哈希表并重新检查重复元素与下标处理"
```

## 目录结构

```text
ai-leetcode-lab/
├─ AGENTS.md                 # 所有 AI 必须遵守的实验协议
├─ ai_leetcode/              # 无第三方依赖的 CLI 实现
├─ archive/
│  ├─ catalog.json           # 全量题目元数据
│  └─ problems/              # 题面、模板等原始归档（JSON）
├─ problems/                 # 开始作答后生成的每题工作目录
├─ data/attempts.jsonl       # 只追加的实验事件
├─ stats/                    # 自动生成的汇总
├─ config/experiment.json    # 尝试预算和同步参数
├─ .ai/identity.env          # 当前 AI 身份，本地保存且不入 Git
└─ .secrets/leetcode.env     # 专用账号凭证，本地保存且不入 Git
```

题目工作目录示例：

```text
problems/0001-two-sum/
├─ meta.json
├─ problem.md
├─ solution.py
└─ approach.md
```

## 身份与署名

`.ai/identity.env` 中的 `AI_CLIENT_NAME` 和 `AI_MODEL_NAME` 会写入新建解答的注释头，也会进入每次事件记录。不同 AI 接手前必须改成自己的真实信息，不能沿用上一个模型的身份。

## 凭证安全

只保存 `csrftoken` 与 `LEETCODE_SESSION`，不保存浏览器的统计、广告或设备 Cookie。`.secrets/` 已被 Git 忽略，pre-commit hook 还会扫描暂存内容中的 LeetCode 会话和常见密钥格式。

如果凭证失效，只替换 `.secrets/leetcode.env`，无需改代码。由于凭证曾经通过聊天传递，实验环境稳定后建议在 LeetCode 重新登录一次并更新本地文件。

## 说明

归档只包含题面、元数据、样例和代码模板，不抓取官方题解、讨论区或他人答案。批量同步是只读操作；远程试跑和正式提交必须通过 CLI，禁止绕过预算直接调用接口。
