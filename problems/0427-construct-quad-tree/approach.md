# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
递归检查区域是否全同；全同建叶子，否则四分并递归建立四个子节点。
## 复杂度
最坏时间 `O(n^2 log n)`，递归空间 `O(log n)`。
## 边界条件与本地验证
单格必为叶子。已构造小网格断言并通过 `py_compile`。
