# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:03:23Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        return max(
            max(i for i in range(len(colors)) if colors[i] != colors[0]),
            len(colors) - 1 - min(i for i in range(len(colors)) if colors[i] != colors[-1]),
        )
