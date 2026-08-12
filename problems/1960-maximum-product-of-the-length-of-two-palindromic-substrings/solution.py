# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:02Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxProduct(self, s: str) -> int:
        def ending_lengths(text):
            n=len(text);radius=[0]*n;left=0;right=-1
            for i in range(n):
                k=1 if i>right else min(radius[left+right-i],right-i+1)
                while i-k>=0 and i+k<n and text[i-k]==text[i+k]:k+=1
                radius[i]=k
                if i+k-1>right:left=i-k+1;right=i+k-1
            end=[0]*n
            for i,k in enumerate(radius):end[i+k-1]=max(end[i+k-1],2*k-1)
            for i in range(n-2,-1,-1):end[i]=max(end[i],end[i+1]-2)
            return end
        left=ending_lengths(s);right=ending_lengths(s[::-1])[::-1]
        for i in range(1,len(s)):left[i]=max(left[i],left[i-1])
        for i in range(len(s)-2,-1,-1):right[i]=max(right[i],right[i+1])
        return max(left[i]*right[i+1] for i in range(len(s)-1))
