# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:07:32Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def splitNum(self, num: int) -> int:
        digits = sorted(str(num))
        return int(''.join(digits[::2])) + int(''.join(digits[1::2]))
