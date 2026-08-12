# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
BFS 后继位置区间按奇偶分组；并查集跳过已访问和禁用位置。
## 复杂度
时间 O(n·α(n))，空间 O(n)。
## 边界条件与本地验证
反转可达位置具有固定奇偶；小 n 直接枚举反转区间核对。
