# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
从右向左尝试增大一位，成功后贪心填入最小的不与前两位冲突字符。
## 复杂度
时间 O(nk)，空间 O(n)。
## 边界条件与本地验证
无后继返回空串；短串枚举字典序核对。
