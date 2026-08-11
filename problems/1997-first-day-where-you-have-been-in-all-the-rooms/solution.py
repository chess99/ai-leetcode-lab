# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        modulo = 1_000_000_007
        first_visit_day = [0] * len(nextVisit)

        for room in range(1, len(nextVisit)):
            first_visit_day[room] = (
                2 * first_visit_day[room - 1] - first_visit_day[nextVisit[room - 1]] + 2
            ) % modulo

        return first_visit_day[-1]
