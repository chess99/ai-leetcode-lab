# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1
## 思路
并查集划分可交换分量，在每个分量内用频次抵消 source 与 target。
## 正确性
同一分量内可任意重排，能抵消的值必可匹配，剩余值必产生差异。
## 复杂度
时间 `O((n+e)α(n))`，空间 `O(n)`。
## 边界条件与本地验证
- 验证了无交换和间接连通。
