# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:23Z
# Experiment: ai-leetcode-lab, round 1
import sys
from typing import List
class Solution:
    def evolutionaryRecord(self, parents: List[int]) -> str:
        sys.setrecursionlimit(max(1000, len(parents) * 2 + 10))
        children = [[] for _ in parents]
        for i in range(1, len(parents)):
            children[parents[i]].append(i)
        def encode(node: int) -> str:
            # Children are ordered by their complete traversal strings.
            return ''.join(sorted('0' + encode(v) + '1' for v in children[node]))
        return encode(0).rstrip('1')
