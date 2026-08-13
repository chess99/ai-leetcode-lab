# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:21Z
# Experiment: ai-leetcode-lab, round 1
# Revised by: Codex Desktop / gpt-5.6-sol / ultra / sol-ultra
from array import array
from typing import Any, Optional

TreeNode = Any


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def getMaxLayerSum(self, root: Optional[TreeNode]) -> int:
        # Preorder numbers are also Euler entry times.  Every subtree is
        # therefore one interval [u, tout[u]].
        parent = []
        depth = []
        tout = []
        delta = []
        eligible = []
        eligible_prefix = []
        levels = []
        layer_sum = []

        stack = [(root, -1, 0)]
        while stack:
            node, p, d = stack.pop()
            u = len(parent)
            parent.append(p)
            depth.append(d)

            left, right = node.left, node.right
            delta.append(
                (left.val if left is not None else 0)
                + (right.val if right is not None else 0)
                - node.val
            )
            can_delete = left is None or right is None
            eligible.append(can_delete)
            eligible_prefix.append(
                (eligible_prefix[p] if p >= 0 else 0) + int(can_delete)
            )

            if d == len(levels):
                levels.append([])
                layer_sum.append(0)
            levels[d].append(u)
            layer_sum[d] += node.val

            # Right first, so that the preorder numbers still visit left first.
            if right is not None:
                stack.append((right, u, d + 1))
            if left is not None:
                stack.append((left, u, d + 1))

        n = len(parent)
        subtree_size = [1] * n
        for u in range(n - 1, 0, -1):
            subtree_size[parent[u]] += subtree_size[u]
        tout = [u + subtree_size[u] - 1 for u in range(n)]

        # Compact binary-lifting tables keep the O(n log n) LCA structure well
        # below the memory cost of Python integer lists.
        first = array("i", (p if p >= 0 else 0 for p in parent))
        up = [first]
        for _ in range(1, n.bit_length()):
            prev = up[-1]
            up.append(array("i", (prev[prev[u]] for u in range(n))))

        def lca(a: int, b: int) -> int:
            if a <= b <= tout[a]:
                return a
            if b <= a <= tout[b]:
                return b
            x = a
            for jump in reversed(up):
                y = jump[x]
                if not (y <= b <= tout[y]):
                    x = y
            return parent[x]

        answer = max(layer_sum)
        last_depth = len(levels) - 1

        for d, same_depth in enumerate(levels):
            # Add LCAs of consecutive preorder nodes.  These nodes are exactly
            # enough to form the virtual tree for this depth.
            virtual = list(same_depth)
            for i in range(1, len(same_depth)):
                virtual.append(lca(same_depth[i - 1], same_depth[i]))
            virtual = sorted(set(virtual))

            virtual_parent = [-1] * len(virtual)
            active = []
            for i, u in enumerate(virtual):
                while active and tout[virtual[active[-1]]] < u:
                    active.pop()
                if active:
                    virtual_parent[i] = active[-1]
                active.append(i)

            # For a node x at depth d, child-values minus x.val is its
            # contribution to the change of layer d.  A virtual subtree sum is
            # thus the complete change caused by deleting any suitable node on
            # its incoming compressed path.
            aggregate = [delta[u] if depth[u] == d else 0 for u in virtual]
            for i in range(len(virtual) - 1, 0, -1):
                aggregate[virtual_parent[i]] += aggregate[i]

            best_change = 0  # Choosing not to delete anything.
            for i, u in enumerate(virtual):
                p = virtual_parent[i]
                if p < 0:
                    # At the original deepest level, deleting an ancestor of
                    # every node would remove that level altogether.  An empty
                    # level is not a layer sum and must not compete as zero.
                    if d == last_depth:
                        continue
                    has_deletable = eligible_prefix[u] > 0
                else:
                    has_deletable = (
                        eligible_prefix[u] - eligible_prefix[virtual[p]] > 0
                    )
                if has_deletable and aggregate[i] > best_change:
                    best_change = aggregate[i]

            answer = max(answer, layer_sum[d] + best_change)

        return answer
