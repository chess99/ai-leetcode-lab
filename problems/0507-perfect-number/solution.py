# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:41:46Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        total = 1
        factor = 2
        while factor * factor <= num:
            if num % factor == 0:
                total += factor
                paired = num // factor
                if paired != factor:
                    total += paired
            factor += 1
        return total == num
