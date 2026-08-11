# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:46:45Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def twoSum(self, price: List[int], target: int) -> List[int]:
        left, right = 0, len(price) - 1
        while left < right:
            total = price[left] + price[right]
            if total == target:
                return [price[left], price[right]]
            if total < target:
                left += 1
            else:
                right -= 1
        return []
