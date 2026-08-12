# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:00Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
import sys
class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        sys.setrecursionlimit(max(1_000_000, len(prevRoom) * 2))
        mod=1_000_000_007;n=len(prevRoom);children=[[] for _ in range(n)]
        for room in range(1,n):children[prevRoom[room]].append(room)
        factorial=[1]*(n+1)
        for i in range(1,n+1):factorial[i]=factorial[i-1]*i%mod
        def visit(room):
            size=1;ways=1
            for child in children[room]:
                child_size,child_ways=visit(child);ways=ways*child_ways%mod;ways=ways*pow(factorial[child_size],mod-2,mod)%mod;size+=child_size
            ways=ways*factorial[size-1]%mod
            return size,ways
        return visit(0)[1]
