# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:15:50Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low, high = 0, len(s)
        permutation = []
        for char in s:
            if char == 'I':
                permutation.append(low)
                low += 1
            else:
                permutation.append(high)
                high -= 1
        permutation.append(low)
        return permutation
