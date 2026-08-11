# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
枚举 `(x xor x')` 的 0..k，另一维异或值随之确定，在已见点哈希表中查询。
## 复杂度
时间 `O(nk)`，空间 `O(n)`。
## 边界条件与本地验证
先查后加避免重复计数；k=0 支持重合点。已验证样例。
