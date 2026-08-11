# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:11Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        last_house = {'M': 0, 'P': 0, 'G': 0}
        for house, items in enumerate(garbage):
            for kind in last_house:
                if kind in items:
                    last_house[kind] = house

        prefix_travel = [0]
        for time in travel:
            prefix_travel.append(prefix_travel[-1] + time)

        return sum(map(len, garbage)) + sum(prefix_travel[house] for house in last_house.values())
