# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        count = len(robot)
        infinity = 10 ** 30
        dynamic = [0] + [infinity] * count
        for position, capacity in factory:
            previous = dynamic[:]
            for used in range(1, count + 1):
                distance = 0
                for amount in range(1, min(capacity, used) + 1):
                    distance += abs(robot[used - amount] - position)
                    dynamic[used] = min(dynamic[used],
                                        previous[used - amount] + distance)
        return dynamic[count]
