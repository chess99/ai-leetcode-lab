# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:30:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        result = []
        back = 0

        for num in nums:
            if num == -1:
                back += 1
                result.append(seen[-back] if back <= len(seen) else -1)
            else:
                seen.append(num)
                back = 0

        return result
