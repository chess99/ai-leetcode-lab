# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

使用 DataFrame 的 `head(3)` 直接取得前 3 行。

## 复杂度

返回行数固定，时间与额外空间复杂度均为 O(1)。

## 边界条件与本地验证

不足 3 行时会返回全部已有行。已进行本地 Pandas 断言。
## 思路

使用 head 选取前最多三行。

## 复杂度

时间、空间为输出规模。

## 边界条件与本地验证

覆盖不足三行。
