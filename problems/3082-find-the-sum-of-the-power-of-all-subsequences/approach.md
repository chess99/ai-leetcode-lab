# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
背包 DP 统计和为每个值的子序列，未选择当前数的后续超集贡献翻倍。
## 复杂度
时间 O(nk)，空间 O(k)。
## 边界条件与本地验证
和超过 k 无需记录；小数组枚举子序列与超集核对。
