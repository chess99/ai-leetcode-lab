# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:15:34Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counts=Counter(tiles)
        def dfs():
            total=0
            for char in counts:
                if counts[char]:counts[char]-=1;total+=1+dfs();counts[char]+=1
            return total
        return dfs()
