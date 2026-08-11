# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
初始化时按字典序预生成所有固定长度组合，用下标实现 `next` 与 `hasNext`。
## 复杂度
预生成空间和时间为 `O(C(n,k)k)`，单次操作为 `O(1)`。
## 边界条件与本地验证
覆盖题面迭代序列和组合长度等于字符串长度。
