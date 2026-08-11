# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

字典保存每个仍有效任务的 `(userId, priority)`，最大堆按 `priority`、`taskId` 的降序排列。编辑和删除只更新字典；执行时弹出堆顶并跳过与字典不一致的过期项。

## 复杂度

每次堆操作为摊销 `O(log q)`，字典查询为 `O(1)`，空间 `O(q)`。

## 边界条件与本地验证

验证编辑后旧堆项失效、删除后跳过、同优先级按较大任务号执行和空队列。
