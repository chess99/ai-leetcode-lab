# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

按值收集位置；循环数组中的最近相同元素必为排序位置表的前驱或后继。

## 复杂度

时间 `O(n+q)`，空间 `O(n)`。

## 边界条件与本地验证

覆盖只出现一次和首尾环绕距离。
