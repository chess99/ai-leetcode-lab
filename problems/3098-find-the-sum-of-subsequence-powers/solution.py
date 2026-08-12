# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        nums.sort()
        modulus = 1_000_000_007
        differences = sorted({nums[j] - nums[i]
                              for i in range(len(nums))
                              for j in range(i + 1, len(nums))})

        def count_at_least(distance):
            previous = [1] * len(nums)
            for _ in range(2, k + 1):
                current = [0] * len(nums)
                prefix = 0
                left = 0
                for right in range(len(nums)):
                    while left < right and nums[right] - nums[left] >= distance:
                        prefix = (prefix + previous[left]) % modulus
                        left += 1
                    current[right] = prefix
                previous = current
            return sum(previous) % modulus

        answer = 0
        counts = [count_at_least(distance) for distance in differences]
        counts.append(0)
        for index, distance in enumerate(differences):
            answer = (answer + distance * (counts[index] - counts[index + 1])) % modulus
        return answer
