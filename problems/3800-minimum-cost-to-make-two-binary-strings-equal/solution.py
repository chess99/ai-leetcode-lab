# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:34Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:
        quintovira = (s, t, flipCost, swapCost, crossCost)
        first_type = second_type = 0
        for a, b in zip(s, t):
            if a == b:
                continue
            if a == '0':
                first_type += 1
            else:
                second_type += 1

        opposite_pairs = min(first_type, second_type)
        same_pairs = (first_type - opposite_pairs) // 2 + (second_type - opposite_pairs) // 2
        singles = (first_type + second_type) % 2
        opposite_cost = min(swapCost, 2 * flipCost)
        same_cost = min(swapCost + crossCost, 2 * flipCost)
        return opposite_pairs * opposite_cost + same_pairs * same_cost + singles * flipCost
