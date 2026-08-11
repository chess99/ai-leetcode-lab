# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
转小写后按词长稳定排序，最后首字母大写。
## 复杂度
时间 `O(N log N)`，空间 `O(N)`。
## 边界条件与本地验证
相同长度词保持原顺序。
