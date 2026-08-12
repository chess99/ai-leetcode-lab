# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
固定后缀数值为 `suffix`，任意候选可写成 `prefix * 10^len(s) + suffix`。对上界 `x`，先得到允许的最大 `prefix=(x-suffix)//10^len(s)`，再按十进制数位 DP 统计不超过该前缀且每位不超过 `limit` 的前缀数量；区间答案用两个上界计数相减。
## 复杂度
时间 O(位数)，空间 O(1)。
## 边界条件与本地验证
`x<suffix` 时没有候选；前缀 0 对应数字本身就是后缀。下界用前缀差；随机短范围逐数检查后缀和每位限制通过。
