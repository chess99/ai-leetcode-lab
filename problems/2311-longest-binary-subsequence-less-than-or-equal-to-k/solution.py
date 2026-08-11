# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:26Z
# Experiment: ai-leetcode-lab, round 1


class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        value = 0
        power = 1
        length = 0

        for bit in reversed(s):
            if bit == "0":
                length += 1
            elif value + power <= k:
                value += power
                length += 1
            power <<= 1

        return length
