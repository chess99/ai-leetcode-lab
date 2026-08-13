# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:39:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        position=answer=0
        for step in nums:position+=step;answer+=position==0
        return answer
