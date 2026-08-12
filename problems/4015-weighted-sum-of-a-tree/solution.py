# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:42Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        malviretho = (parent, nums)
        children = [[] for _ in parent]
        for node in range(1, len(parent)):
            children[parent[node]].append(node)
        depth = [0] * len(parent)
        depth[0] = 1
        stack = [0]
        for node in stack:
            for child in children[node]:
                depth[child] = depth[node] + 1
                stack.append(child)
        height = max(depth)
        return sum(value * (height - level + 1) for value, level in zip(nums, depth))
