# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def transportationHub(self, path: List[List[int]]) -> int:
        nodes = set()
        incoming = {}
        outgoing = set()
        for start, end in path:
            nodes.update((start, end))
            outgoing.add(start)
            incoming.setdefault(end, set()).add(start)
        for node in nodes:
            if node not in outgoing and len(incoming.get(node, ())) == len(nodes) - 1:
                return node
        return -1
