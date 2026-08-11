# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:45:04Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        positions = {char: index for index, char in enumerate(t)}
        return sum(abs(index - positions[char]) for index, char in enumerate(s))
