# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:03:06Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        candidates = set(bank)
        if endGene not in candidates:
            return -1
        queue = deque([(startGene, 0)])
        while queue:
            gene, steps = queue.popleft()
            for index, original in enumerate(gene):
                for base in "ACGT":
                    if base == original:
                        continue
                    mutated = gene[:index] + base + gene[index + 1:]
                    if mutated == endGene:
                        return steps + 1
                    if mutated in candidates:
                        candidates.remove(mutated)
                        queue.append((mutated, steps + 1))
        return -1
