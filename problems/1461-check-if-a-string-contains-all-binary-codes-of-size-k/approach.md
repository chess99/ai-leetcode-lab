# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
收集所有长度为 k 的子串，集合大小为 `2^k` 时覆盖全部二进制码。
## 复杂度
时间 `O(Nk)`，空间 `O(Nk)`。
## 边界条件与本地验证
长度不足时自然返回 false。
