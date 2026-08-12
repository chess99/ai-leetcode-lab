# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:43Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sumScores(self, s: str) -> int:
        size = len(s)
        z = [0] * size
        left = right = 0
        for index in range(1, size):
            if index <= right:
                z[index] = min(right - index + 1, z[index - left])
            while index + z[index] < size and s[z[index]] == s[index + z[index]]:
                z[index] += 1
            if index + z[index] - 1 > right:
                left = index
                right = index + z[index] - 1
        return size + sum(z)
