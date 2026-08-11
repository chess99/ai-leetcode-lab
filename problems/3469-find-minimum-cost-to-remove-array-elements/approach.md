# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

递归状态保留前三元素中未删除的一个值，枚举三种保留选择并记忆化。

## 复杂度

时间 `O(n)`，空间 `O(n)`。

## 边界条件与本地验证

覆盖不足三个元素及题面两个示例。
