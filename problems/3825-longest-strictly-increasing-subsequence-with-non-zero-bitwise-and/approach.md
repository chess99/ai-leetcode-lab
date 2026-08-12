# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

子序列按位与非零等价于存在某一位被所有元素共同包含。枚举 30 个二进制位，过滤含该位的元素并求严格 LIS，取最大长度。

## 复杂度

时间 `O(30n log n)`，空间 `O(n)`。

## 边界条件与本地验证

零不含任何位；严格递增用 `bisect_left`。保留隐藏变量，覆盖三组示例。
