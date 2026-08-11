# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:45:55Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        for first_end in range(1, len(num) - 1):
            if num[0] == "0" and first_end > 1: break
            for second_end in range(first_end + 1, len(num)):
                if num[first_end] == "0" and second_end - first_end > 1: break
                first, second, index = int(num[:first_end]), int(num[first_end:second_end]), second_end
                while index < len(num):
                    total = str(first + second)
                    if not num.startswith(total, index): break
                    first, second, index = second, first + second, index + len(total)
                if index == len(num): return True
        return False
