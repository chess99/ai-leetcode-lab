# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:23Z
# Experiment: ai-leetcode-lab, round 1

from __future__ import annotations

from typing import Optional



class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        parents = {root.val: (None, "")}
        stack = [root]

        while stack:
            node = stack.pop()
            if node.left:
                parents[node.left.val] = (node.val, "L")
                stack.append(node.left)
            if node.right:
                parents[node.right.val] = (node.val, "R")
                stack.append(node.right)

        def path_from_root(value: int) -> str:
            directions = []
            while parents[value][0] is not None:
                parent, direction = parents[value]
                directions.append(direction)
                value = parent
            return "".join(reversed(directions))

        start_path = path_from_root(startValue)
        dest_path = path_from_root(destValue)
        common_length = 0
        while (
            common_length < len(start_path)
            and common_length < len(dest_path)
            and start_path[common_length] == dest_path[common_length]
        ):
            common_length += 1

        return "U" * (len(start_path) - common_length) + dest_path[common_length:]
