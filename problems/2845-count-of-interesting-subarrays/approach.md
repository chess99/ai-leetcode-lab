# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
前缀记录满足 `num % modulo == k` 的数量模 modulo；哈希表统计可配对的旧余数。
## 复杂度
时间 `O(n)`，空间 `O(modulo)`。
## 边界条件与本地验证
初始余数 0 出现一次；已验证题面样例。
