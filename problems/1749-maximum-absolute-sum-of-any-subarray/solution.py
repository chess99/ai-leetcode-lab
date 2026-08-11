# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix=highest=lowest=answer=0
        for value in nums:
            prefix+=value;answer=max(answer,prefix-lowest,highest-prefix);highest=max(highest,prefix);lowest=min(lowest,prefix)
        return answer
