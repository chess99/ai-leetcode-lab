# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
按值收集下标，对每组下标滑窗，使两端间非该值元素数不超过 k。
## 复杂度
时间 `O(n)`，空间 `O(n)`。
## 边界条件与本地验证
同值连续时无需删除；已验证题面样例。
