# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

枚举实际使用的舞台数 `j`。把 `n` 个人分成 `j` 个非空无标号组有第二类 Stirling 数 `S(n,j)`；从 `x` 个舞台选择并排列 `j` 个是下降阶乘；每个已用舞台有 `y` 种分数。累加 `S(n,j)*(x)_j*y^j`。

## 复杂度

一维 Stirling DP 时间 `O(n*min(n,x))`，空间 `O(min(n,x))`。

## 边界条件与本地验证

未使用舞台不评分，实际舞台数不超过 `min(n,x)`。3 组样例及小规模枚举每个人舞台分配通过，`n=x=1000` 约 0.08 秒。
