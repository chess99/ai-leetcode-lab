# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

位置可任意调整，因此只需比较两种颜色的数量。记录 source 的颜色计数，遍历 target 时没有可匹配颜色的无人机必须切换。

## 复杂度

时间复杂度 O(nm)，额外空间复杂度 O(不同颜色数)。

## 边界条件与本地验证

颜色出现次数差异会逐个产生切换。已进行 Python 语法检查及最小断言。
