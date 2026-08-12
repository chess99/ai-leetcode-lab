# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:45Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left,right=1,m*n
        while left<right:
            mid=(left+right)//2
            if sum(min(mid//i,n)for i in range(1,m+1))>=k:right=mid
            else:left=mid+1
        return left
