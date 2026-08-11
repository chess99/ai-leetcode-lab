# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors=[0]*n; pairs=0; ans=[]
        for i,color in queries:
            if colors[i]:
                pairs-=i>0 and colors[i]==colors[i-1]; pairs-=i+1<n and colors[i]==colors[i+1]
            colors[i]=color
            pairs+=i>0 and color==colors[i-1]; pairs+=i+1<n and color==colors[i+1]
            ans.append(pairs)
        return ans
