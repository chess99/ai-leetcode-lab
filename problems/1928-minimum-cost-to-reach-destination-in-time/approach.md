# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

按总时间 DP，转移每条双向边到达端点的最低费用，最后取终点所有可行时间的最小值。

## 复杂度

时间 O(maxTime·E)，空间 O(maxTime·V)。

## 边界条件与本地验证

起点费用需计入；小图按时间状态最短路核对。
