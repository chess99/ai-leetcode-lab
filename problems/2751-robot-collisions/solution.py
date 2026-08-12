# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        order = sorted(range(len(positions)), key=positions.__getitem__)
        right_moving = []
        for index in order:
            if directions[index] == 'R':
                right_moving.append(index)
                continue
            while right_moving and healths[index] > 0:
                other = right_moving[-1]
                if healths[other] < healths[index]:
                    healths[other] = 0
                    healths[index] -= 1
                    right_moving.pop()
                elif healths[other] > healths[index]:
                    healths[other] -= 1
                    healths[index] = 0
                else:
                    healths[other] = healths[index] = 0
                    right_moving.pop()
        return [health for health in healths if health > 0]
