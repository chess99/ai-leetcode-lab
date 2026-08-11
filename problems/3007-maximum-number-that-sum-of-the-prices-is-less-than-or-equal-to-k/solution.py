# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:36Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def total_price(number: int) -> int:
            total = 0
            position = x
            while position <= 60:
                half = 1 << (position - 1)
                cycle = half << 1
                total += (number + 1) // cycle * half + max(0, (number + 1) % cycle - half)
                position += x
            return total

        low, high = 0, 10**18
        while low < high:
            mid = (low + high + 1) // 2
            if total_price(mid) <= k:
                low = mid
            else:
                high = mid - 1
        return low
