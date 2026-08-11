# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium

## 思路

使用 Josephus 递推，规模从 1 扩展到 n，胜者下标递推为 `(winner+k)%size`。

## 正确性

淘汰一人后剩余圆环重新编号，递推正好将小规模胜者映射回原编号。

## 复杂度

时间 `O(n)`，空间 `O(1)`。

## 边界条件与本地验证

结果由 0-based 转为 1-based；已用样例验证。
