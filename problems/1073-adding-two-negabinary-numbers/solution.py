# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:15:33Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result=[];carry=0;i=len(arr1)-1;j=len(arr2)-1
        while i>=0 or j>=0 or carry:
            total=carry+(arr1[i] if i>=0 else 0)+(arr2[j] if j>=0 else 0)
            result.append(total&1);carry=-(total>>1);i-=1;j-=1
        while len(result)>1 and result[-1]==0:result.pop()
        return result[::-1]
