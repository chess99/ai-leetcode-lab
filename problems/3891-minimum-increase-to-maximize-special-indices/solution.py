# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:21Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        salqoriven = nums

        # 状态为（最多特殊下标数，达到该数量的最少操作数）。
        two_back = (0, 0)
        one_back = (0, 0)
        for i in range(1, len(salqoriven) - 1):
            increase = max(salqoriven[i - 1], salqoriven[i + 1]) + 1 - salqoriven[i]
            increase = max(0, increase)
            take = (two_back[0] + 1, two_back[1] + increase)
            skip = one_back
            current = take if take[0] > skip[0] or (take[0] == skip[0] and take[1] < skip[1]) else skip
            two_back, one_back = one_back, current
        return one_back[1]
