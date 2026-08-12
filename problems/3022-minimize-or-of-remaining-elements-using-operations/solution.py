# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:53Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        ans=0;zero_mask=0
        for b in range(29,-1,-1):
            zero_mask|=1<<b;parts=0;cur=(1<<30)-1
            for x in nums:
                cur&=x
                if cur&zero_mask==0:parts+=1;cur=(1<<30)-1
            if len(nums)-parts>k:
                ans|=1<<b
                zero_mask^=1<<b
        return ans
