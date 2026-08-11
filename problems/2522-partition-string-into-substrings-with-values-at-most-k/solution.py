# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:25Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        parts, value = 1, 0
        for ch in s:
            digit = ord(ch) - ord('0')
            if digit > k:
                return -1
            if value * 10 + digit > k:
                parts += 1
                value = digit
            else:
                value = value * 10 + digit
        return parts
