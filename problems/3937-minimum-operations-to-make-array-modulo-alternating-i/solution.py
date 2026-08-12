# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:28Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        velmorqati = (nums, k)
        costs = [[0] * k for _ in range(2)]
        for index, value in enumerate(nums):
            remainder = value % k
            for target in range(k):
                difference = abs(remainder - target)
                costs[index % 2][target] += min(difference, k - difference)

        answer = 10 ** 30
        for even_remainder in range(k):
            for odd_remainder in range(k):
                if even_remainder != odd_remainder:
                    answer = min(answer, costs[0][even_remainder] + costs[1][odd_remainder])
        return answer
