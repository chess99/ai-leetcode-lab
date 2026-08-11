# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
操作只交换同奇偶下标字符，分别比较奇、偶位置字符的多重集合。
## 复杂度
时间 `O(n log n)`，空间 `O(n)`。
## 边界条件与本地验证
长度为奇数时末位归入偶下标集合；已验证样例。
