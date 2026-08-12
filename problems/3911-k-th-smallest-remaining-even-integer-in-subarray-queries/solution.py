# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:37Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def kthRemainingInteger(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        import bisect
        odd=[0]
        for x in nums:odd.append(odd[-1]+(x&1))
        ans=[]
        for l,r,k in queries:
            def removed(t):
                end=bisect.bisect_right(nums,2*t,l,r+1)
                return (end-l)-(odd[end]-odd[l])
            lo,hi=1,k+r-l+1
            while lo<hi:
                mid=(lo+hi)//2
                if mid-removed(mid)>=k:hi=mid
                else:lo=mid+1
            ans.append(2*lo)
        return ans
