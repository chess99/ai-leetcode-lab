# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

树形 DFS 合并子树。子树内部方案相乘，再用组合数交错排列各子树建造顺序。

## 复杂度

时间 O(n log MOD)，空间 O(n)。

## 边界条件与本地验证

提高深链递归限制；小树枚举满足父先于子的排列核对。
