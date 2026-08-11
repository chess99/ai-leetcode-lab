# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total=answer=0
        for i,x in enumerate(nums): total+=x; answer=max(answer,(total+i)//(i+1))
        return answer
