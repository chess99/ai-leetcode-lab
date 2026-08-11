# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:15:50Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(any(strs[row][column] > strs[row + 1][column]
                       for row in range(len(strs) - 1))
                   for column in range(len(strs[0])))
