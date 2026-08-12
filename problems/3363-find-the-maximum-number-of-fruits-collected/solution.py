# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:58:10Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n=len(fruits);ans=sum(fruits[i][i] for i in range(n));neg=-10**18
        def side(reverse):
            dp=[neg]*n;dp[n-1]=fruits[0][n-1]
            for i in range(1,n):
                nd=[neg]*n
                for j in range(max(i,n-1-i),n):
                    col=n-1-j if reverse else j
                    value=0 if i==j else fruits[i][col]
                    nd[j]=value+max(dp[max(0,j-1):min(n,j+2)])
                dp=nd
            return dp[n-1]
        return ans+side(False)+side(True)
