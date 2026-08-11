# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
队列广度优先遍历，每轮固定当前队列长度收集一层并加入所有子节点。
## 复杂度
时间 `O(n)`，空间 `O(n)`。
## 边界条件与本地验证
空树返回空。已构造三级树断言并通过 `py_compile`。
