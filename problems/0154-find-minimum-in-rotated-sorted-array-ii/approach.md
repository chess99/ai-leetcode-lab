# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

比较中点与右端，确定最小值所在半区；相等时右端缩一格排除重复歧义。

## 复杂度

一般 O(log n)，全重复最坏 O(n)，空间 O(1)。

## 边界条件与本地验证

不旋转和单元素数组同样适用。
