# 解题记录

- 初始创建：Codex Desktop / gpt-5.6-terra / medium / terra-medium
- 本轮接手：Codex Desktop / gpt-5.6-sol / medium / sol-medium
- 接手原因：terra-medium 远判失败；输出只将 `id` 改为 `student_id`，期望四列全部重命名
- 轮次：1

## 根因

Terra 的映射是 `{'id': 'student_id', 'name': 'first_name'}`。输入表不存在 `name` 列，真实源列名是 `first`；同时 `last` 和 `age` 没有出现在映射中。因此 pandas 只执行了 `id` 的重命名，得到不完整表头。

## 思路

调用 `DataFrame.rename(columns=...)`，一次提供题目要求的四个精确映射：

- `id → student_id`
- `first → first_name`
- `last → last_name`
- `age → age_in_years`

不使用 `inplace=True`，直接返回重命名后的 DataFrame。该操作只改变列标签，不改变行顺序、索引、单元格值或各列数据类型，输入 DataFrame 的原列名也保持不变。

## 正确性说明

输入模式恰好包含 `id、first、last、age` 四列。映射的定义域覆盖全部四个原列名，映射值依次是题目指定的四个新列名。`rename(columns=...)` 对每个命中的列标签应用对应替换，并保留列的原顺序，所以结果表头必为 `[student_id, first_name, last_name, age_in_years]`；由于没有执行筛选、排序或值赋值，结果中的每一行数据与输入对应行完全一致。

## 复杂度

设列数为 `c`、行数为 `r`。列标签映射本身需要 `O(c)` 时间；pandas 返回新 DataFrame 时的具体数据复制取决于版本和复制策略，按可能复制底层数据的保守上界，时间与空间均为 `O(rc)`。本题固定为 4 列。

## 本地验证

- 使用题面 5 行样例执行函数，验证完整表头及全部值。
- 验证空 DataFrame 仍得到四个正确列名。
- 使用自定义索引和明确 dtype 的 DataFrame，验证索引、值、列顺序和 dtype 均保持不变。
- 验证函数调用后原 DataFrame 的列名未被原地修改。
