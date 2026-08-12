# 解题思路

> 作者：Codex Desktop · gpt-5.6-terra · medium（terra-medium）

## 思路

## 等价变形

设矩阵有 `m` 行、`n` 列，第 `i` 行和第 `j` 列中 `1` 的数量分别为 `row_ones[i]`、`col_ones[j]`。由于一行共有 `n` 个位置、一列共有 `m` 个位置：

```text
zerosRow[i] = n - row_ones[i]
zerosCol[j] = m - col_ones[j]
```

代入题目公式可得：

```text
diff[i][j] = 2 * row_ones[i] + 2 * col_ones[j] - m - n
```

因此不需要逐格重复统计零的数量。

## 算法

1. 一次遍历各行，得到每行 `1` 的数目。
2. 统计每列 `1` 的数目。
3. 对每个位置按化简后的公式直接计算答案。

## 正确性证明

对任意位置 `(i, j)`，第 `i` 行的零数等于 `n - row_ones[i]`，第 `j` 列的零数等于 `m - col_ones[j]`。将这两个等式代入题目定义，得到算法使用的公式 `2 * row_ones[i] + 2 * col_ones[j] - m - n`。算法预先统计的行、列一数均准确，并对每个位置应用该等价公式，所以每个 `diff[i][j]` 都正确，返回的整个矩阵正确。

## 复杂度分析

- 时间复杂度：`O(mn)`。
- 空间复杂度：`O(m + n)`，不计返回矩阵。
