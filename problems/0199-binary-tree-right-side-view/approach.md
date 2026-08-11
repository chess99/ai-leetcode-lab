# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
按层广度遍历，每层最后一个节点就是右视图可见节点。
## 复杂度
- 时间 O(n)，空间 O(n)。
## 边界条件与本地验证
- 空树返回空数组。验证 `[1,2,3,null,5,null,4] -> [1,3,4]`。
