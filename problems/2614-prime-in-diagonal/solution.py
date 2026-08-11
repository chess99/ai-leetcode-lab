# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:10:09Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def is_prime(value):
            if value < 2:
                return False
            divisor = 2
            while divisor * divisor <= value:
                if value % divisor == 0:
                    return False
                divisor += 1
            return True
        size = len(nums)
        return max((nums[row][column] for row in range(size) for column in (row, size - 1 - row) if is_prime(nums[row][column])), default=0)
