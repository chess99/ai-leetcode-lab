# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:03Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        from collections import Counter
        cnt = Counter(nums); mod = 10**9 + 7
        primes = [2,3,5,7,11,13,17,19,23,29]
        masks = {}
        for x in range(2,31):
            y=x; mask=0; ok=True
            for i,p in enumerate(primes):
                if y%(p*p)==0: ok=False; break
                if y%p==0: mask|=1<<i
            if ok: masks[x]=mask
        dp=[0]*1024; dp[0]=pow(2,cnt[1],mod)
        for x,mask in masks.items():
            for state in range(1023,-1,-1):
                if not state&mask: dp[state|mask]=(dp[state|mask]+dp[state]*cnt[x])%mod
        return (sum(dp)-dp[0])%mod
