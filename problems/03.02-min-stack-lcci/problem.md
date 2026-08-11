# 面试题 03.02. 栈的最小值

- 难度：EASY
- 标签：栈, 设计
- 来源：https://leetcode.cn/problems/min-stack-lcci/
- 归档：2026-08-11T15:56:58Z

## 题目

<p>请设计一个栈，除了常规栈支持的pop与push函数以外，还支持min函数，该函数返回栈元素中的最小值。执行push、pop和min操作的时间复杂度必须为O(1)。</p><br><p><strong>示例：</strong><pre>MinStack minStack = new MinStack();<br>minStack.push(-2);<br>minStack.push(0);<br>minStack.push(-3);<br>minStack.getMin();   --> 返回 -3.<br>minStack.pop();<br>minStack.top();      --> 返回 0.<br>minStack.getMin();   --> 返回 -2.</pre></p>

## 样例输入

```text
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
```
