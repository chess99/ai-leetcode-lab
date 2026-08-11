# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:22:20Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isFascinating(self, n: int) -> bool:
        digits = str(n) + str(2 * n) + str(3 * n)
        return len(digits) == 9 and set(digits) == set("123456789")
