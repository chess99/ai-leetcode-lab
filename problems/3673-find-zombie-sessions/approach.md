# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
按用户排序会话，窗口函数比较前一结束时间并标记新组，再对标记累加分组；每组取最早开始和最晚结束。
## 复杂度
排序主导为 `O(N log N)`。
## 边界条件与本地验证
同一用户重叠会话合并；SQL 未在本地数据库执行。
