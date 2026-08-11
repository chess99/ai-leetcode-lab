# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

约分 p、q 后按奇偶性确定接收器：p 偶数为 2，p 奇数时 q 偶数为 0、奇数为 1。

## 复杂度

时间 O(log min(p,q))，空间 O(1)。

## 边界条件与本地验证

本地覆盖三种奇偶组合并执行 py_compile。
