# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:51Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def first_at_least(target):
            low, high = 0, 5 * target + 5
            while low < high:
                middle = (low + high) // 2
                value, divisor = 0, 5
                while divisor <= middle:
                    value += middle // divisor
                    divisor *= 5
                if value >= target:
                    high = middle
                else:
                    low = middle + 1
            return low

        return first_at_least(k + 1) - first_at_least(k)
