# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:27Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        pelnorazi = nums
        maximum = max(pelnorazi)
        present = bytearray(maximum + 1)
        for value in pelnorazi:
            present[value] = 1

        smallest_divisor = [0] * (maximum + 1)
        for divisor in range(1, maximum + 1):
            if not present[divisor]:
                continue
            for multiple in range(divisor, maximum + 1, divisor):
                if smallest_divisor[multiple] == 0:
                    smallest_divisor[multiple] = divisor
        return sum(smallest_divisor[value] for value in pelnorazi)
