# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
先取不互为 target 补数的最小前半段，再从 target 起连续取剩余数，使用等差数列求和。
## 复杂度
时间和空间均为 `O(1)`。
## 边界条件与本地验证
结果按模数返回；已验证小规模样例。
