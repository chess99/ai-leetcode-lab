# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路
枚举可能的 gcd `g`，遍历数组值域中 `g` 的所有倍数，并对实际存在的倍数持续求 gcd。若结果降到 `g`，这些数可组成 gcd 为 `g` 的子序列。

## 复杂度
设最大值为 $M$，时间 $O(M\log M)$，空间 $O(M)$。

## 边界条件与本地验证
重复值只需标记存在。已与小数组全部非空子序列的 gcd 集合对拍。
