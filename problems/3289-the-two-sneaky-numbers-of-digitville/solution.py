# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:57:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        result = []
        for num in nums:
            if num in seen:
                result.append(num)
            else:
                seen.add(num)
        return result
