# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:15:48Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = 1
        for even in range(0, len(nums), 2):
            if nums[even] % 2:
                while nums[odd] % 2:
                    odd += 2
                nums[even], nums[odd] = nums[odd], nums[even]
        return nums
