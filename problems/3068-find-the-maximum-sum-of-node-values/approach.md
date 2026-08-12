# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
每个节点取异或后的增益，选取正增益中数量为偶数的最大总和。
## 复杂度
时间 O(n log n)，空间 O(n)。
## 边界条件与本地验证
边数不影响可达偶数选择；小树枚举边操作核对。
