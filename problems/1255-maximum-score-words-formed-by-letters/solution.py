# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        from collections import Counter
        available=Counter(letters);best=0
        def dfs(i,total):
            nonlocal best
            if i==len(words):best=max(best,total);return
            dfs(i+1,total);need=Counter(words[i])
            if all(need[c]<=available[c]for c in need):
                available.subtract(need);dfs(i+1,total+sum(score[ord(c)-97]*v for c,v in need.items()));available.update(need)
        dfs(0,0);return best
