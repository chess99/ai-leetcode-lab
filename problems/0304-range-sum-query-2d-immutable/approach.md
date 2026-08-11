# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
构造二维前缀和，容斥在 O(1) 求任意子矩形。
## 复杂度
- 预处理 O(mn)，查询 O(1)，空间 O(mn)。
## 边界条件与本地验证
- 前缀数组补零边界。验证题例三次查询为 8、11、12。
