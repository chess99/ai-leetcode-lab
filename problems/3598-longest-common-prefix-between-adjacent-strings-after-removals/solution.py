# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        def lcp(a, b):
            i = 0
            while i < len(a) and i < len(b) and a[i] == b[i]: i += 1
            return i
        pair = [lcp(words[i], words[i + 1]) for i in range(n - 1)]
        pref = [0] * n
        for i, value in enumerate(pair): pref[i + 1] = max(pref[i], value)
        suff = [0] * n
        for i in range(n - 2, -1, -1): suff[i] = max(suff[i + 1], pair[i])
        ans = []
        for i in range(n):
            best = max(pref[max(0, i - 1)], suff[min(n - 1, i + 1)])
            if 0 < i < n - 1: best = max(best, lcp(words[i - 1], words[i + 1]))
            ans.append(best)
        return ans
