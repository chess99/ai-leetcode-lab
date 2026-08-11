# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:59:42Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        from math import gcd, lcm
        answer = 0
        for start in range(len(nums)):
            product = 1
            common_gcd = 0
            common_lcm = 1
            for end in range(start, len(nums)):
                product *= nums[end]
                common_gcd = gcd(common_gcd, nums[end])
                common_lcm = lcm(common_lcm, nums[end])
                if product == common_gcd * common_lcm:
                    answer = max(answer, end - start + 1)
        return answer
