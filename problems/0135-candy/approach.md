# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

两次扫描分别满足左邻和右邻约束，每个位置取两次要求的较大值。

## 复杂度

时间 O(n)，空间 O(n)。

## 边界条件与本地验证

相等评分无需增加糖果，空数组返回零。
