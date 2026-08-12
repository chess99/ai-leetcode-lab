# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:23Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from math import gcd


class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        n=len(nums)
        logs=[0]*(n+1)
        for i in range(2,n+1):logs[i]=logs[i//2]+1
        st=[nums]
        step=1
        while step*2<=n:
            old=st[-1];st.append([gcd(old[i],old[i+step]) for i in range(n-step*2+1)])
            step*=2
        def range_gcd(left,right):
            length=right-left+1;p=logs[length]
            return gcd(st[p][left],st[p][right-(1<<p)+1])
        def possible(length):
            # A modification breaks every stable interval containing it. Greedy
            # on earliest-ending bad intervals is optimal interval stabbing.
            changes=0; last=-1
            for i in range(length,n):
                if i-length > last and range_gcd(i-length,i)>=2:
                    changes+=1;last=i;g=0
            return changes<=maxC
        lo,hi=0,n
        while lo<hi:
            mid=(lo+hi)//2
            if possible(mid):hi=mid
            else:lo=mid+1
        return lo
