# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

将 Person 自连接。对于同一 email，若某行 id 大于另一行 id，则删除较大 id 的那一行；因此每个邮箱只保留最小 id。

## 复杂度

时间复杂度 O(N²)（未计索引优化），空间复杂度 O(1)。

## 边界条件与本地验证

唯一邮箱没有匹配行不会被删除；重复两次或多次时只有最小 id 保留；比较使用严格大于，避免删除保留行。
