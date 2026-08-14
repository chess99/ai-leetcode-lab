# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Created: 2026-08-14
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def canEat(
        self, candiesCount: List[int], queries: List[List[int]]
    ) -> List[bool]:
        prefix = [0]
        for count in candiesCount:
            prefix.append(prefix[-1] + count)

        answer = []
        for favorite_type, favorite_day, daily_cap in queries:
            first_target = prefix[favorite_type] + 1
            last_target = prefix[favorite_type + 1]
            earliest_on_day = favorite_day + 1
            latest_on_day = (favorite_day + 1) * daily_cap
            answer.append(
                first_target <= latest_on_day
                and earliest_on_day <= last_target
            )
        return answer
