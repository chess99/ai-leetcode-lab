# 2887. 填充缺失值

- 难度：EASY
- 标签：无
- 来源：https://leetcode.cn/problems/fill-missing-data/
- 归档：2026-08-11T14:28:08Z

## 题目

<pre>
DataFrame <code>products</code>
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| quantity    | int    |
| price       | int    |
+-------------+--------+
</pre>

<p>编写一个解决方案，在 <code>quantity</code> 列中将缺失的值填充为&nbsp;<code><strong>0</strong></code>。</p>

<p>返回结果如下示例所示。</p>

<p>&nbsp;</p>
<strong class="example">示例 1：</strong>

<pre>
<strong>输入：
</strong>+-----------------+----------+-------+
| name            | quantity | price |
+-----------------+----------+-------+
| Wristwatch      | 32       | 135   |
| WirelessEarbuds | None     | 821   |
| GolfClubs       | None     | 9319  |
| Printer         | 849      | 3051  |
+-----------------+----------+-------+
<strong>输出：
</strong>+-----------------+----------+-------+
| name            | quantity | price |
+-----------------+----------+-------+
| Wristwatch      | 32       | 135   |
| WirelessEarbuds | 0        | 821   |
| GolfClubs       | 0        | 9319  |
| Printer         | 849      | 3051  |
+-----------------+----------+-------+
<b>解释：</b>
Toaster 和 Headphones 的数量被填充为 0。</pre>


## 样例输入

```text
{"headers":{"products":["name","quantity","price"]},"rows":{"products":[["Wristwatch",null,135],["WirelessEarbuds",null,821],["GolfClubs",779,9319],["Printer",849,3051]]}}
```
