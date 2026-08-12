# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

按成本排序并预处理容量前缀最大值。枚举较高下标机器，二分严格满足伙伴成本 `< budget-current` 的最右位置，并限制伙伴在当前之前；同时考虑只选一台。

## 复杂度

时间 `O(n log n)`，空间 `O(n)`。

## 边界条件与本地验证

预算为严格上界，二分使用 `bisect_left`；可能一台也买不起，此时返回 0。保留隐藏变量，覆盖三组示例。
