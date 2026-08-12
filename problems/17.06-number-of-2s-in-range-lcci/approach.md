# 解题记录

- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium；轮次：1

## 思路

逐十进制位统计。将 n 相对当前 factor 拆为 higher、current、lower：完整高位周期贡献 `higher*factor`；current 等于 2 时再贡献 `lower+1`，大于 2 时贡献完整 factor。

## 复杂度

时间 `O(log n)`，空间 `O(1)`。

## 边界条件与本地验证

n=0 返回 0，22 会在个位和十位各计一次。官方 25 得到 9；n=0..2999 与逐数转字符串计数 oracle 全部一致。
