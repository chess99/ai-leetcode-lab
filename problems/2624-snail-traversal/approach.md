# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

先验证数组长度是否等于 `rowsCount * colsCount`。随后按列填充：偶数列从上到下，奇数列从下到上；原数组在每列内的连续 `rowsCount` 个元素正好对应当前方向。

## 复杂度

时间 `O(rowsCount * colsCount)`，输出矩阵占同等 `O(rowsCount * colsCount)` 空间。

## 边界条件与本地验证

长度不匹配直接返回空数组。单行或单列仍按相同公式工作；奇数列使用 `rowsCount - 1 - row` 翻转目标行。
