# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        groups=[set()for _ in range(26)]
        for s in ideas:groups[ord(s[0])-97].add(s[1:])
        ans=0
        for i in range(26):
            for j in range(i):
                c=len(groups[i]&groups[j]);ans+=2*(len(groups[i])-c)*(len(groups[j])-c)
        return ans
