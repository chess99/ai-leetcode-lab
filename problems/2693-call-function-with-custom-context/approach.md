# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
将原函数临时挂到 context 的唯一 Symbol 属性上，以方法调用形式传入 this，调用后删除临时属性。
## 复杂度
时间 `O(args.length)`，额外空间 `O(1)`。
## 边界条件与本地验证
Symbol 不会与已有属性冲突；已验证返回值及参数转发。
