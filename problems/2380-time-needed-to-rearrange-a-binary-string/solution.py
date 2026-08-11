# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:09Z
# Experiment: ai-leetcode-lab, round 1


class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        zeros = 0
        seconds = 0
        for char in s:
            if char == "0":
                zeros += 1
            elif zeros:
                seconds = max(seconds + 1, zeros)
        return seconds
