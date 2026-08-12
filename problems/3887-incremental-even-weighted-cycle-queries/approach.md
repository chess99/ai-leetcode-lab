# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

带异或势能的并查集维护每点到根的边权异或。新边连接不同连通块时可加入；同块时它形成的环权值奇偶由两点势能与新边权异或确定，偶数才计入。

## 复杂度

`O(q alpha(n))` 时间，`O(n)` 空间。

## 边界条件与本地验证

已 importlib 加载；三角形权值均为 1 的样例返回 2。
