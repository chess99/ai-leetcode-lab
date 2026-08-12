# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
分解每个数的不同质因子，出现相同质因子的下标并查集合并。
## 复杂度
时间 O(n√V)，空间 O(n+质因子数)。
## 边界条件与本地验证
单元素为真，含一且长度大于一为假；小数组建 gcd 图核对。
