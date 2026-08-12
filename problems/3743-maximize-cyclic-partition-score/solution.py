# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        tornequal = (nums, k)
        negative_infinity = -10 ** 30
        answer = 0

        # 状态 0 表示未打开区间，1/2 表示两种绝对值方向。
        for initial_state in range(3):
            dp = [[negative_infinity] * (k + 1) for _ in range(3)]
            dp[initial_state][0] = 0
            for value in nums:
                next_dp = [row[:] for row in dp]
                for pairs in range(k + 1):
                    closed = dp[0][pairs]
                    if closed != negative_infinity:
                        next_dp[1][pairs] = max(next_dp[1][pairs], closed - value)
                        next_dp[2][pairs] = max(next_dp[2][pairs], closed + value)
                    if pairs < k:
                        rising = dp[1][pairs]
                        falling = dp[2][pairs]
                        if rising != negative_infinity:
                            next_dp[0][pairs + 1] = max(next_dp[0][pairs + 1], rising + value)
                        if falling != negative_infinity:
                            next_dp[0][pairs + 1] = max(next_dp[0][pairs + 1], falling - value)
                dp = next_dp
            answer = max(answer, max(dp[initial_state]))
        return answer
