# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路
用一维 DP 记录每一步后处于各下标的方案数，每轮从当前位置向左、停留、向右转移。最远不可能超过总步数，因此截断有效数组长度。

## 复杂度
时间 `O(steps·min(arrLen,steps))`，空间 `O(min(arrLen,steps))`。

## 边界条件
所有结果取模；长度为 1 时只能原地停留；越界转移直接忽略。
