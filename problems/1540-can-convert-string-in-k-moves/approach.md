# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
统计各非零循环位移出现次数，第 n 次相同位移只能在 `d+26(n-1)` 时执行。
## 复杂度
时间 `O(N)`，空间 `O(26)`。
## 边界条件与本地验证
长度不同直接失败。
