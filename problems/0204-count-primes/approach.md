# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
埃氏筛：标记小于 n 的数为候选素数，对每个未标记合数的数从平方开始筛去倍数。
## 复杂度
- 时间 O(n log log n)，空间 O(n)。
## 边界条件与本地验证
- `n<3` 返回 0。验证 `10 -> 4`、`0 -> 0`、`100 -> 25`。
