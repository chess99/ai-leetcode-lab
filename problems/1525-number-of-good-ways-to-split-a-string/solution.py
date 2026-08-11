# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:55:39Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
class Solution:
    def numSplits(self, s: str) -> int:
        left=set();right=Counter(s);answer=0
        for char in s[:-1]:
            left.add(char);right[char]-=1
            if not right[char]:del right[char]
            if len(left)==len(right):answer+=1
        return answer
