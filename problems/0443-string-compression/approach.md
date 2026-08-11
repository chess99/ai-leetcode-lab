# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium；轮次：1
## 思路
读指针扫描连续组，写指针原地写字符与多位计数。
## 复杂度
时间 `O(n)`，空间 `O(1)`。
## 边界条件与本地验证
- 单字符不写计数；断言示例前缀为 `a2b2c3`。
