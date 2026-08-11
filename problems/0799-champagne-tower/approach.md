# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

逐行模拟，杯中超过一的部分均分给下一行相邻两杯，查询时截断到一。

## 复杂度

时间 `O(r^2)`，空间 `O(r)`。

## 边界条件与本地验证

- 零溢出与满杯均覆盖；已完成 `py_compile` 和断言。
