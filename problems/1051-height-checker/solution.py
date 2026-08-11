# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:27:34Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(actual != expected for actual, expected in zip(heights, sorted(heights)))
