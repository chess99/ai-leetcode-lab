# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:27Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        blocked=set(forbidden);limit=max([x]+forbidden)+a+b;queue=deque([(0,False,0)]);seen={(0,False)}
        while queue:
            position,backward,steps=queue.popleft()
            if position==x:return steps
            for nxt,is_backward in ((position+a,False),(position-b,True)):
                if nxt<0 or nxt>limit or nxt in blocked or (is_backward and backward) or (nxt,is_backward) in seen:continue
                seen.add((nxt,is_backward));queue.append((nxt,is_backward,steps+1))
        return -1
