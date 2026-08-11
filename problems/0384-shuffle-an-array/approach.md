# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

保存原数组副本。每次 shuffle 在新副本上执行 Fisher-Yates：从后向前，为当前位置均匀随机选择前缀中的一个位置交换。每种排列概率相等；reset 返回原始顺序的副本。

## 复杂度

shuffle 时间 `O(n)`、返回数组空间 `O(n)`；reset 同样复制 `O(n)`。

## 边界条件与本地验证

- 不暴露内部原数组，调用方修改返回值不影响后续 reset。
- 单元素洗牌不变。
- 本地断言：reset 恢复原序，shuffle 输出保留同一元素集合。
