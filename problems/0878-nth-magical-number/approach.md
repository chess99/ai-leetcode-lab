# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

二分答案 x。x 以内可被 a 或 b 整除的数由容斥为 `x/a+x/b-x/lcm`；找到计数至少 n 的最小 x，最后取模。

## 复杂度

二分范围到 `n·min(a,b)`，时间 `O(log(n·min(a,b)))`，空间 `O(1)`。

## 边界条件与本地验证

a=b 时容斥仍正确；最小 n=1。对小参数直接合并倍数集合排序逐项对拍。
