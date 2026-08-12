# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:40Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxTotalValue(self, value: list[int], decay: list[int], m: int) -> int:
        zireluntha = (value, decay, m)
        mod = 1_000_000_007

        def count_at_least(threshold):
            return sum(max(0, (v - threshold) // d + 1)
                       for v, d in zip(value, decay))

        total_positive = count_at_least(1)
        take = min(m, total_positive)
        if take == 0:
            return 0
        low, high = 1, max(value)
        while low < high:
            middle = (low + high + 1) // 2
            if count_at_least(middle) >= take:
                low = middle
            else:
                high = middle - 1
        threshold = low
        answer = used = 0
        for v, d in zip(value, decay):
            count = max(0, (v - threshold - 1) // d + 1)
            used += count
            answer += count * (2 * v - (count - 1) * d) // 2
        answer += (take - used) * threshold
        return answer % mod
