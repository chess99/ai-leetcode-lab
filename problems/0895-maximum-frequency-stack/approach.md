# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

哈希表记录每值频率，频率映射到压栈序列；pop 从最高频率组尾部取值实现同频最近优先。

## 复杂度

push、pop 均摊 O(1)，空间 O(n)。

## 边界条件与本地验证

最高频率组清空后下降一级；重复值独立保留入栈顺序。
