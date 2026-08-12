# 面试题 04.06. 后继者

- 难度：MEDIUM
- 标签：树, 深度优先搜索, 二叉搜索树, 二叉树
- 来源：https://leetcode.cn/problems/successor-lcci/
- 归档：2026-08-12T05:00:51Z

## 题目

<p>设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。</p>

<p>如果指定节点没有对应的“下一个”节点，则返回<code>null</code>。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>root = <code>[2,1,3], p = 1

  2
 / \
1   3
</code>
<strong>输出：</strong>2</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = <code>[5,3,6,2,4,null,null,1], p = 6

      5
     / \
    3   6
   / \
  2   4
 /
1
</code>
<strong>输出：</strong>null</pre>


## 样例输入

```text
[2,1,3]
1
```
