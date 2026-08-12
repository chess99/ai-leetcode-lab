# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

除 pos 外的 n-1 人中，任意 k 人恰好选择使 pos 可见的方向，其余方向固定；pos 自身有 2 种选择。因此答案为 2*C(n-1,k)。用阶乘与费马逆元求组合数。

## 复杂度

时间 O(n + log MOD)，空间 O(n)。

## 边界条件与本地验证

验证 k=0、k=n-1 和题目样例。
