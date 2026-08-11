# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

先排除 `null`、`undefined` 与非函数的类参数。随后从对象的原型开始向上遍历原型链，只要遇到 `classFunction.prototype` 就说明该值是此类或其子类的实例。

## 复杂度

时间为原型链长度 `O(h)`，额外空间 `O(1)`。

## 边界条件与本地验证

不直接使用 `instanceof`，因此可安全处理基本类型；`Object.getPrototypeOf(5)` 可得到 `Number.prototype`。函数本身、`null` 与 `undefined` 不会被误判为实例。
