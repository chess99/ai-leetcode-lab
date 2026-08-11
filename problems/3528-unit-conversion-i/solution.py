# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:53Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List

class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for source, target, factor in conversions:
            graph[source].append((target, factor))
        result = [0] * (len(conversions) + 1)
        result[0] = 1
        stack = [0]
        mod = 10**9 + 7
        while stack:
            source = stack.pop()
            for target, factor in graph[source]:
                result[target] = result[source] * factor % mod
                stack.append(target)
        return result
