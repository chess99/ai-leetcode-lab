# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
先以零为根统计正确猜测，换根时仅反转父子边猜测的贡献。
## 复杂度
时间 O(n+猜测数)，空间 O(n)。
## 边界条件与本地验证
覆盖 k 为零；小树逐根 DFS 核对。
