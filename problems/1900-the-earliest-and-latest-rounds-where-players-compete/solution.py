# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:51:59Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache
from typing import List
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        firstPlayer-=1;secondPlayer-=1
        @lru_cache(None)
        def play(players):
            players=list(players);games=len(players)//2;options=[[]]
            for i in range(games):
                a,b=players[i],players[-1-i]
                if {a,b}=={firstPlayer,secondPlayer}:return (1,1)
                winners=[a] if a in (firstPlayer,secondPlayer) else [b] if b in (firstPlayer,secondPlayer) else [a,b]
                options=[chosen+[winner] for chosen in options for winner in winners]
            if len(players)%2:options=[chosen+[players[games]] for chosen in options]
            results=[play(tuple(sorted(chosen))) for chosen in options]
            return (1+min(x for x,y in results),1+max(y for x,y in results))
        return list(play(tuple(range(n))))
