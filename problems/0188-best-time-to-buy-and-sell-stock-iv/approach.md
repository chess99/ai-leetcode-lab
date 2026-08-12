# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

维护每笔交易的买入与卖出状态；k 足够大时退化为累加全部正价差。

## 复杂度

时间 O(nk)，空间 O(k)。

## 边界条件与本地验证

空数组和 k 为零返回零。
