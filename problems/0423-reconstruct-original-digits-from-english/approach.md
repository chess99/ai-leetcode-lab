# 解题记录
- AI 客户端：Codex Desktop；模型：gpt-5.6-terra；推理档位：medium；Profile：terra-medium
## 思路
利用唯一字母依次确定 0、2、4、6、8，再消减计数确定其余数字。
## 复杂度
时间 `O(n)`，空间 `O(1)`。
## 边界条件与本地验证
输出须升序。已断言 `owoztneoer -> 012` 并通过 `py_compile`。
