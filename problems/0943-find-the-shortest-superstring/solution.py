# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:03Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n=len(words);dp={(1<<i,i):words[i]for i in range(n)}
        def join(a,b):
            for k in range(min(len(a),len(b)),-1,-1):
                if a.endswith(b[:k]):return a+b[k:]
        for mask in range(1,1<<n):
            for last in range(n):
                if (mask,last) in dp:
                    for nxt in range(n):
                        if not mask>>nxt&1:
                            key=(mask|1<<nxt,nxt);v=join(dp[mask,last],words[nxt])
                            if key not in dp or len(v)<len(dp[key]):dp[key]=v
        return min((dp[(1 << n) - 1, i] for i in range(n)), key=len)
