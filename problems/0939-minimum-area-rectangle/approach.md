# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

按列枚举同列两点，记录该纵坐标对上次出现的列；再次出现即构成矩形并更新面积。

## 复杂度

时间为各列点对数，空间为不同点对数。

## 边界条件与本地验证

- 无矩形返回零；已完成 `py_compile` 和断言。
