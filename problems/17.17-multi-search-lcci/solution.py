# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:22:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        root = {}
        result = [[] for _ in smalls]
        for index, word in enumerate(smalls):
            if not word:
                continue
            node = root
            for char in word:
                node = node.setdefault(char, {})
            node.setdefault("#", []).append(index)
        for start in range(len(big)):
            node = root
            for end in range(start, len(big)):
                if big[end] not in node:
                    break
                node = node[big[end]]
                for index in node.get("#", []):
                    result[index].append(start)
        return result
