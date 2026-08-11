# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
固定长度滑动窗口维护元素和，与 `k * threshold` 比较。
## 复杂度
时间 `O(N)`，空间 `O(1)`。
## 边界条件与本地验证
覆盖单窗口和所有窗口均不满足。
