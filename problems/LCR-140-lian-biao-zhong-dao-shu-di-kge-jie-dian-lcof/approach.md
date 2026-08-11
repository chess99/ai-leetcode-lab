# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

快指针先走 cnt 步，再与慢指针同步前进，快指针到尾时慢指针即为答案。

## 复杂度

时间复杂度 O(n)，额外空间复杂度 O(1)。

## 边界条件与本地验证

cnt 保证合法。已进行 Python 语法检查及最小断言。
