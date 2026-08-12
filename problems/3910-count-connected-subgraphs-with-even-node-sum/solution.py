# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:36Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        n=len(nums);adj=[0]*n
        for a,b in edges:adj[a]|=1<<b;adj[b]|=1<<a
        ans=0
        for mask in range(1,1<<n):
            if sum(nums[i] for i in range(n) if mask>>i&1)&1:continue
            seen=mask&-mask;front=seen
            while front:
                bit=front&-front;front-=bit;i=bit.bit_length()-1
                add=adj[i]&mask&~seen;seen|=add;front|=add
            ans+=seen==mask
        return ans
