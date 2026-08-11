# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
从小到大贪心选数，若其补数 `k-x` 已选则跳过。
## 复杂度
时间和空间均为 `O(n+k)`。
## 边界条件与本地验证
互异元素的补数检查即可；已验证题面样例。
