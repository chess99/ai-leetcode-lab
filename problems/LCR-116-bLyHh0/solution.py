# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:29Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        provinces = 0
        for city in range(len(isConnected)):
            if city in seen:
                continue
            provinces += 1
            stack = [city]
            seen.add(city)
            while stack:
                current = stack.pop()
                for neighbor, connected in enumerate(isConnected[current]):
                    if connected and neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
        return provinces
