# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
在升序数组二分第一个满足 `citations[i] >= n-i` 的位置；其右侧论文数即 h。
## 复杂度
- 时间 O(log n)，空间 O(1)。
## 边界条件与本地验证
- 无满足位置时 h 为 0。验证 `[0,1,3,5,6] -> 3`、`[1,2,100] -> 2`。
