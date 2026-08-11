# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:21Z
# Experiment: ai-leetcode-lab, round 1

from collections import defaultdict
from typing import List


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        """自底向上汇总代表人数，并计算每条向上道路所需车辆数。"""
        n = len(roads) + 1
        graph = defaultdict(list)
        for city_a, city_b in roads:
            graph[city_a].append(city_b)
            graph[city_b].append(city_a)

        parent = [-1] * n
        parent[0] = 0
        order = [0]
        for city in order:
            for neighbor in graph[city]:
                if parent[neighbor] == -1:
                    parent[neighbor] = city
                    order.append(neighbor)

        representatives = [1] * n
        fuel = 0
        for city in reversed(order[1:]):
            people = representatives[city]
            fuel += (people + seats - 1) // seats
            representatives[parent[city]] += people
        return fuel
