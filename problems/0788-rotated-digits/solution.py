# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:44:44Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def rotatedDigits(self, n: int) -> int:
        unchanged = {"0", "1", "8"}
        changed = {"2", "5", "6", "9"}
        count = 0
        for value in range(1, n + 1):
            digits = set(str(value))
            if digits <= unchanged | changed and digits & changed:
                count += 1
        return count
