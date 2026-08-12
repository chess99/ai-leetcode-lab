# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:49Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def defendSpaceCity(self, time: List[int], position: List[int]) -> int:
        state_count = 1 << 5

        def barrier_cost(mask: int, opening_cost: int) -> int:
            cost = 0
            previous = False
            for bit in range(5):
                active = bool(mask & (1 << bit))
                if active:
                    cost += 1 if previous else opening_cost
                previous = active
            return cost

        single_cost = [barrier_cost(mask, 2) for mask in range(state_count)]
        joint_cost = [barrier_cost(mask, 3) for mask in range(state_count)]
        # 末尾补一个空舱室，让最后一个位置开启的联合屏障能正常结算。
        required = [0] * (max(position) + 2)
        for moment, cabin in zip(time, position):
            required[cabin] |= 1 << (moment - 1)

        infinity = 10**9
        dp = [infinity] * state_count
        dp[0] = 0
        for meteor_mask in required:
            next_dp = [infinity] * state_count
            for left_mask, current_cost in enumerate(dp):
                if current_cost == infinity:
                    continue
                for right_mask in range(state_count):
                    blocked = left_mask | right_mask
                    if left_mask & right_mask:
                        continue
                    needed = meteor_mask & ~blocked
                    best_single = infinity
                    for single_mask in range(state_count):
                        if single_mask & blocked == 0 and single_mask & needed == needed:
                            best_single = min(best_single, single_cost[single_mask])
                    candidate = current_cost + joint_cost[right_mask] + best_single
                    next_dp[right_mask] = min(next_dp[right_mask], candidate)
            dp = next_dp
        return dp[0]
