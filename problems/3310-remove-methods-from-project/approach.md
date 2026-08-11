# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

从可疑方法沿调用图搜索所有可疑方法。若存在正常方法调用任何可疑方法，则无法安全移除；否则返回全部非可疑方法。

## 复杂度

时间 `O(n + invocations.length)`，空间 `O(n + invocations.length)`。

## 边界条件与本地验证

覆盖无外部调用、外部调用可疑方法和可疑调用链。
