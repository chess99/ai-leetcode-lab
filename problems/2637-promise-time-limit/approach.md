# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

构造一个在 `t` 毫秒后以固定字符串拒绝的 Promise，并与延后调用 `fn(...args)` 得到的 Promise 使用 `Promise.race` 竞争。先完成者决定包装函数的结果。

## 复杂度

创建包装调用的同步开销为 `O(1)`，额外空间 `O(1)`（不计底层 Promise 与计时器）。

## 边界条件与本地验证

使用 `Promise.resolve().then(...)` 能把原函数同步抛出的异常转换为拒绝。若原函数先拒绝，原错误原样传播；超过或达到限时而仍未完成时拒绝为 `"Time Limit Exceeded"`。
