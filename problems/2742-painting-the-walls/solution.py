# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:40Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        count = len(cost)
        infinity = 10 ** 15
        dynamic = [0] + [infinity] * count
        for price, free_time in zip(cost, time):
            previous = dynamic[:]
            covered = free_time + 1
            for walls in range(1, count + 1):
                dynamic[walls] = min(dynamic[walls],
                                     previous[max(0, walls - covered)] + price)
        return dynamic[count]
