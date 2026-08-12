# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

字典保存活跃事件的最新优先级，堆保存 (-priority,eventId)。更新时压入新记录；取出时丢弃与字典不一致的过期记录，命中后删除字典项。

## 复杂度

每次操作摊还 O(log n)，空间 O(n+q)。

## 边界条件与本地验证

验证优先级并列时较小 id、重复更新和空管理器。
