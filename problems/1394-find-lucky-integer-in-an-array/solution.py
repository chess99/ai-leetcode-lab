# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:58:06Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = {}
        for value in arr:
            counts[value] = counts.get(value, 0) + 1
        return max((value for value, count in counts.items() if value == count), default=-1)
