# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
双指针扫描，字符等于目标或循环加一后等于目标时匹配下一位。
## 复杂度
时间 `O(|str1|)`，空间 `O(1)`。
## 边界条件与本地验证
处理 `z` 循环到 `a`；已验证题面样例。
