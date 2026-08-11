# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:26:46Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        ways = [0] * n
        ways[0] = 1
        for _ in range(k):
            next_ways = [0] * n
            for source, target in relation:
                next_ways[target] += ways[source]
            ways = next_ways
        return ways[n - 1]
