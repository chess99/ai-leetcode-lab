# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
迭代中序遍历 BST，弹出第 k 个节点即第 k 小元素。
## 复杂度
- 时间 O(h+k)，空间 O(h)。
## 边界条件与本地验证
- k 从 1 计数。验证 `[3,1,4,null,2],1 -> 1` 和第二示例 k=3 -> 3。
