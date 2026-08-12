# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

按题面要求用 `sorivandek` 保存输入。依次枚举 top、left、right、bottom，逐层检查已经确定的角字符约束并保证四个单词互异；收集后按四元组字典序排序。

## 复杂度

单词数 `m≤15`，最坏时间 `O(m⁴)`，结果空间不计时额外递归空间 `O(1)`。

## 边界条件与本地验证

输入单词本身互异，但四个角色仍需显式互异。验证两个题面样例。
