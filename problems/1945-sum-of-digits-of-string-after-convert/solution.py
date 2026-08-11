# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:56:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        total = sum(sum(map(int, str(ord(char) - ord('a') + 1))) for char in s)
        for _ in range(k - 1):
            total = sum(map(int, str(total)))
        return total
