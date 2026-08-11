# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

按时间排序，并让同一时刻的 `OFFLINE` 排在消息前。`online_until` 记录每名用户恢复在线的时刻；`ALL` 直接累加全体，`HERE` 只累加已恢复在线者，显式 id 逐个计数。

## 复杂度

时间 `O(e log e + eu)`，空间 `O(u)`；题目用户数很小。

## 边界条件与本地验证

验证同一时刻离线先于消息、离线满 60 时重新在线、ALL 包含离线者和重复 id。
