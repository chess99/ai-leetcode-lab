# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:58:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        from bisect import bisect_left
        arr=sorted((r,l,w,i) for i,(l,r,w) in enumerate(intervals));ends=[x[0] for x in arr];dp=[[(0,())for _ in range(5)]for _ in range(len(arr)+1)]
        for i,(r,l,w,idx) in enumerate(arr,1):
            p=bisect_left(ends,l)
            for q in range(5):
                dp[i][q]=dp[i-1][q]
                if q:
                    cand=(dp[p][q-1][0]+w,tuple(sorted(dp[p][q-1][1]+(idx,))))
                    if cand[0]>dp[i][q][0] or cand[0]==dp[i][q][0] and cand[1]<dp[i][q][1]:dp[i][q]=cand
        return list(max(dp[-1],key=lambda x:(x[0],tuple(-z for z in x[1])))[1])
