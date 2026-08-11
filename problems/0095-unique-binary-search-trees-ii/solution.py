# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:18:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List, Optional


class Solution:
    def generateTrees(self, n: int) -> List[Optional["TreeNode"]]:
        def build(lower: int, upper: int) -> List[Optional["TreeNode"]]:
            if lower > upper:
                return [None]
            trees = []
            for root_value in range(lower, upper + 1):
                for left in build(lower, root_value - 1):
                    for right in build(root_value + 1, upper):
                        trees.append(TreeNode(root_value, left, right))
            return trees

        return build(1, n)
