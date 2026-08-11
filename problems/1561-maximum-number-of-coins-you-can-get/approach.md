# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
排序后 Bob 取最小三分之一；余下部分每轮 Alice 取最大、我取次大，故隔一个累加。
## 正确性
保留最小值给 Bob 可使我每次可选值最大，贪心最优。
## 复杂度
时间 `O(n log n)`，空间 `O(1)`（忽略排序）。
## 边界条件与本地验证
- 验证了三堆和题目示例。
