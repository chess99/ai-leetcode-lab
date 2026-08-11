# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:24:47Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = ''.join(char for char in number if char.isdigit())
        groups = []
        while len(digits) > 4:
            groups.append(digits[:3])
            digits = digits[3:]
        if len(digits) == 4:
            groups.extend((digits[:2], digits[2:]))
        else:
            groups.append(digits)
        return '-'.join(groups)
