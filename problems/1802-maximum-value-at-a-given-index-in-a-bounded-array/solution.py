# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:31Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def side_sum(peak: int, length: int) -> int:
            if peak > length:
                return (peak - 1 + peak - length) * length // 2
            return (peak - 1) * peak // 2 + (length - peak + 1)

        low, high = 1, maxSum
        while low < high:
            peak = (low + high + 1) // 2
            required_sum = peak + side_sum(peak, index) + side_sum(peak, n - index - 1)
            if required_sum <= maxSum:
                low = peak
            else:
                high = peak - 1

        return low
