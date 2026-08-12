# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:49Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        seen=set();ans=1
        for x in rolls:
            seen.add(x)
            if len(seen)==k:ans+=1;seen.clear()
        return ans
