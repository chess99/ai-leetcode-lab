# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
枚举被左移 k 位的元素，用前缀 OR 与后缀 OR 在 `O(1)` 组合其余元素。
## 复杂度
时间 `O(n)`，空间 `O(n)`。
## 边界条件与本地验证
`k=0` 仍正确；使用整数位运算。已验证题面样例。
