# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:16:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        provinces = 0
        for city in range(len(isConnected)):
            if city in visited:
                continue
            provinces += 1
            stack = [city]
            visited.add(city)
            while stack:
                current = stack.pop()
                for neighbor, connected in enumerate(isConnected[current]):
                    if connected and neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
        return provinces
