# 2879. 显示前三行

- 难度：EASY
- 标签：无
- 来源：https://leetcode.cn/problems/display-the-first-three-rows/
- 归档：2026-08-11T14:27:49Z

## 题目

<pre>
DataFrame: <code>employees</code>
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| employee_id | int    |
| name        | object |
| department  | object |
| salary      | int    |
+-------------+--------+
</pre>

<p>编写一个解决方案，显示这个 DataFrame 的<strong> 前&nbsp;&nbsp;<code>3</code>&nbsp;</strong>行。</p>

<p>&nbsp;</p>

<p><b>示例 1:</b></p>

<pre>
<strong>输入：
</strong>DataFrame employees
+-------------+-----------+-----------------------+--------+
| employee_id | name      | department            | salary |
+-------------+-----------+-----------------------+--------+
| 3           | Bob       | Operations            | 48675  |
| 90          | Alice     | Sales                 | 11096  |
| 9           | Tatiana   | Engineering           | 33805  |
| 60          | Annabelle | InformationTechnology | 37678  |
| 49          | Jonathan  | HumanResources        | 23793  |
| 43          | Khaled    | Administration        | 40454  |
+-------------+-----------+-----------------------+--------+
<b>输出：</b>
+-------------+---------+-------------+--------+
| employee_id | name    | department  | salary |
+-------------+---------+-------------+--------+
| 3           | Bob     | Operations  | 48675  |
| 90          | Alice   | Sales       | 11096  |
| 9           | Tatiana | Engineering | 33805  |
+-------------+---------+-------------+--------+
<b>解释：</b>
只有前 3 行被显示。</pre>


## 样例输入

```text
{"headers":{"employees":["employee_id","name","department","salary"]},"rows":{"employees":[[3,"Bob","Operations",48675],[90,"Alice","Sales",11096],[9,"Tatiana","Engineering",33805],[60,"Annabelle","InformationTechnology",37678],[49,"Jonathan","HumanResources",23793],[43,"Khaled","Administration",40454]]}}
```
