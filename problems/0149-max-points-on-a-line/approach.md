# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

固定每个起点，用约分并规范符号后的方向向量统计共线点数。

## 复杂度

时间 O(n²)，空间 O(n)。

## 边界条件与本地验证

重复点单独累计，水平和竖直方向统一表示。
