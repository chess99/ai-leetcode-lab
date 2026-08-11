# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:08Z
# Experiment: ai-leetcode-lab, round 1


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        best = [0] * 26
        for char in s:
            index = ord(char) - ord("a")
            length = 1 + max(best[max(0, index - k) : min(26, index + k + 1)])
            best[index] = max(best[index], length)
        return max(best)
