# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

自连接 Stadium 三次枚举以当前记录为中心的连续三个 id，要求三条记录人数均不少于一百，再 DISTINCT 返回所有参与记录。

## 复杂度

连接规模受表和索引影响，结果按 visit_date 排序。

## 边界条件与本地验证

仅本题是 MySQL；三种相对位置覆盖连续段的首中尾，重复命中由 DISTINCT 消除。
