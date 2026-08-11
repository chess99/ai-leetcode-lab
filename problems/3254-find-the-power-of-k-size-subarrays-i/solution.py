# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        answer = []
        for start in range(len(nums) - k + 1):
            valid = all(nums[index] == nums[index - 1] + 1 for index in range(start + 1, start + k))
            answer.append(nums[start + k - 1] if valid else -1)
        return answer
