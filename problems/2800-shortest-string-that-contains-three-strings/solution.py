# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:15Z
# Experiment: ai-leetcode-lab, round 1
from itertools import permutations
class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def join(x,y):
            if y in x:return x
            for i in range(min(len(x),len(y)),-1,-1):
                if x.endswith(y[:i]): return x+y[i:]
        best=None
        for p in permutations((a,b,c)):
            value=join(join(p[0],p[1]),p[2])
            if best is None or (len(value),value)<(len(best),best):best=value
        return best
