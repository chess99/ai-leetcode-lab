# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
用 Z 函数计算每个后缀和原串的公共前缀，检查 k 的倍数位是否覆盖剩余串。
## 复杂度
时间 O(n)，空间 O(n)。
## 边界条件与本地验证
无提前匹配时向上取整；短串直接比较后缀核对。
