# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

维护长度为 rowIndex + 1 的数组，首尾保持为 1。逐行从右向左更新内部位置，使每个位置累加其左侧旧值；倒序更新避免覆盖仍需读取的上一行数据。

## 复杂度

时间 O(rowIndex²)，空间 O(rowIndex)。

## 边界条件与本地验证

rowIndex 为 0 时直接返回 [1]；倒序更新确保计算下一项时左侧仍是上一行值。本地检查第 0、1、3 和 4 行。
