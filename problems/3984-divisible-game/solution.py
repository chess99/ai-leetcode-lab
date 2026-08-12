# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:36Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def divisibleGame(self, nums: list[int]) -> int:
        ravontelix = nums
        positions = {}
        for i, value in enumerate(nums):
            d = 1
            while d * d <= value:
                if value % d == 0:
                    if d > 1:
                        positions.setdefault(d, []).append((i, value))
                    other = value // d
                    if other != d and other > 1:
                        positions.setdefault(other, []).append((i, value))
                d += 1

        # An optimal non-empty segment starts and ends at values divisible by k.
        # Between consecutive such values, every element contributes negatively.
        best, chosen = -min(nums), 2
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        for divisor, items in positions.items():
            current = None
            previous = -1
            for index, value in items:
                if current is None:
                    current = value
                else:
                    gap = prefix[index] - prefix[previous + 1]
                    current = value + max(0, current - gap)
                previous = index
                if current > best or (current == best and divisor < chosen):
                    best, chosen = current, divisor
        return best * chosen % 1_000_000_007
