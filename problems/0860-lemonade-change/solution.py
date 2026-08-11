# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:05:26Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            elif ten and five:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
        return True
