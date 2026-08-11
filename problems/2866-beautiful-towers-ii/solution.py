# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n=len(maxHeights); left=[0]*n; stack=[]
        for i,h in enumerate(maxHeights):
            while stack and maxHeights[stack[-1]]>h: stack.pop()
            left[i]=h*(i-(stack[-1] if stack else -1))+(left[stack[-1]] if stack else 0); stack.append(i)
        right=[0]*n; stack=[]; answer=0
        for i in range(n-1,-1,-1):
            h=maxHeights[i]
            while stack and maxHeights[stack[-1]]>h: stack.pop()
            right[i]=h*((stack[-1] if stack else n)-i)+(right[stack[-1]] if stack else 0); stack.append(i)
            answer=max(answer,left[i]+right[i]-h)
        return answer
