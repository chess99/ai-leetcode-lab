# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

先假设全部使用技巧 2，改用技巧 1 的收益变化为 `technique1[i]-technique2[i]`。按变化从大到小排序：前 `k` 个必须选择，其余仅选择正收益变化。按题面要求用 `caridomesh` 保存输入。

## 复杂度

时间 `O(n log n)`，空间 `O(n)`。

## 边界条件与本地验证

`k=0` 时只取所有正收益变化；即使前 `k` 个变化为负也必须选择。验证三个题面样例。
