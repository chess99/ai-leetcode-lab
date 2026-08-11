# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

末端 j 可搭配的首端范围为 [0, j-m+1]。扫描 j 时维护该范围的最小和最大首端值，与 nums[j] 相乘取最大。

## 复杂度

时间 O(n)，空间 O(1)；m=1 时首尾为同一元素。

## 边界条件与本地验证

待填写。
