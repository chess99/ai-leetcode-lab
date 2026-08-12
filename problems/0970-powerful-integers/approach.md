# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

枚举不超过 bound 的 x、y 幂次并用集合去重。

## 复杂度

时间为幂次组合数，空间为结果数。

## 边界条件与本地验证

- x/y 为一时循环仍会终止（受 bound）；完成 `py_compile` 和断言。
