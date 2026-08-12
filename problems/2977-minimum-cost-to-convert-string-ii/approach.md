# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
对规则字符串做全源最短路，再按长度切分位置动态规划。
## 复杂度
时间 O(W³+nL)，空间 O(W²)。
## 边界条件与本地验证
相同字符可直接延续；不可转换返回负一。
