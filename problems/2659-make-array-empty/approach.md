# 解题记录
- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
## 思路
按值和下标排序，Fenwick 树维护未删除位置数，计算每次旋转至下一个最小值的经过元素数。
## 复杂度
时间 O(n log n)，空间 O(n)。
## 边界条件与本地验证
处理重复值及跨越数组尾部；小数组队列模拟核对。
