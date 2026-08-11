# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

每行保留限制数目的最大元素，再从全部候选中取全局前 k 个。

## 复杂度

时间 `O(总元素 log k)`，空间 `O(总候选数)`。

## 边界条件与本地验证

覆盖行限制为零及 k 小于候选数。
