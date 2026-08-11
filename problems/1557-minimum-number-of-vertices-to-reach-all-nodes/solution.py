# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:56:22Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        has_parent = {target for _, target in edges}
        return [node for node in range(n) if node not in has_parent]
