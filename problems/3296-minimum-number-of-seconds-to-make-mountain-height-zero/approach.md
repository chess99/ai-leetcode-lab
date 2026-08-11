# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

二分总时间；工人在时间 `t` 内的工作层数由三角数不等式用整数平方根求得。

## 复杂度

时间 `O(workers.length * log(H^2 * maxWorker))`，空间 `O(1)`。

## 边界条件与本地验证

覆盖单工人、多人分摊和山高为一。
