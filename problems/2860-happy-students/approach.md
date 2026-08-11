# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
排序后枚举选中人数 x，检查左边所有阈值小于 x、右边所有阈值大于 x。
## 复杂度
时间 `O(n log n)`，空间 `O(1)`（不计排序）。
## 边界条件与本地验证
包含选 0 人和选全部人；已验证样例。
