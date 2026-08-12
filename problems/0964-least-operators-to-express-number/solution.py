# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:04Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        positive = negative = 0
        position = 0
        while target:
            target, digit = divmod(target, x)
            cost = 2 if position == 0 else position
            if position == 0:
                positive = digit * cost
                negative = (x - digit) * cost
            else:
                next_positive = min(digit * cost + positive,
                                    (digit + 1) * cost + negative)
                next_negative = min((x - digit) * cost + positive,
                                    (x - digit - 1) * cost + negative)
                positive, negative = next_positive, next_negative
            position += 1
        return min(positive, position + negative) - 1
