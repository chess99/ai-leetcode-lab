# 705. 设计哈希集合

- 难度：EASY
- 标签：设计, 数组, 哈希表, 链表, 哈希函数
- 来源：https://leetcode.cn/problems/design-hashset/
- 归档：2026-08-11T11:04:51Z

## 题目

<p>不使用任何内建的哈希表库设计一个哈希集合（HashSet）。</p>

<p>实现 <code>MyHashSet</code> 类：</p>

<ul>
	<li><code>void add(key)</code> 向哈希集合中插入值 <code>key</code> 。</li>
	<li><code>bool contains(key)</code> 返回哈希集合中是否存在这个值 <code>key</code> 。</li>
	<li><code>void remove(key)</code> 将给定值 <code>key</code> 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。</li>
</ul>
&nbsp;

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
<strong>输出：</strong>
[null, null, null, true, false, null, true, null, false]

<strong>解释：</strong>
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // 返回 True
myHashSet.contains(3); // 返回 False ，（未找到）
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // 返回 True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // 返回 False ，（已移除）</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= key &lt;= 10<sup>6</sup></code></li>
	<li>最多调用 <code>10<sup>4</sup></code> 次 <code>add</code>、<code>remove</code> 和 <code>contains</code></li>
</ul>


## 样例输入

```text
["MyHashSet","add","add","add","remove","contains","add","add","add","remove","contains","add","add","add","remove","contains","add","add","add","remove","contains"]
[[],[1],[10001],[1],[1],[1],[7],[10007],[7],[7],[7],[123],[10123],[123],[123],[123],[5000],[15000],[5000],[5000],[5000]]
```
