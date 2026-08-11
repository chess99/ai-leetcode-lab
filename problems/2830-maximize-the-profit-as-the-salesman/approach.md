# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
按结束房屋分组 offers，DP 决定跳过当前位置或接受以此结束的要约。
## 复杂度
时间 `O(n+offers)`，空间 `O(n+offers)`。
## 边界条件与本地验证
相邻区间可同时选；已验证题面样例。
