# 解题记录

- AI 客户端：Codex Desktop
- 模型：gpt-5.6-terra
- 推理档位：medium
- Profile：terra-medium
- 轮次：1

## 思路

用正则依次抽取带可选正负号的 `分子/分母` 项。维护当前最简分数 `numerator/denominator`；加入 `a/b` 时计算 `numerator*b + a*denominator` 与 `denominator*b`，然后立即用最大公约数约分。立即约分可控制中间数增长。

分母始终为正，分子可以为负；分子为零时 `gcd(0, denominator)` 会把结果正确约为 `0/1`。

## 复杂度

- 设表达式长度为 `L`、分数项数为 `t`。解析为 `O(L)`，每项约分的欧几里得算法为对数级，总时间为 `O(L + t log V)`，`V` 为中间数大小。
- 除正则匹配结果和常数个整数外使用 `O(1)` 工作空间。

## 边界条件与本地验证

- 首项可没有显式 `+` 号，正则仍能识别。
- 加减抵消时返回 `0/1`，而不是带零分母或负零。
- 多位分子、分母和负结果都按整数解析并由 `gcd(abs(numerator), denominator)` 约分。

本地对题目三个示例、多个连续加减项、整数结果和负结果做最小断言，并执行 `py_compile` 语法检查。
