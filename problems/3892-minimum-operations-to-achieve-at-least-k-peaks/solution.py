# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:35Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if k == 0:
            return 0
        if k > n // 2:
            return -1
        cost = [max(0, max(nums[(i - 1) % n], nums[(i + 1) % n]) + 1 - nums[i]) for i in range(n)]
        inf = 10**30

        def solve(first_taken: bool) -> int:
            dp0 = [inf] * (k + 1)
            dp1 = [inf] * (k + 1)
            if first_taken:
                dp1[1] = cost[0]
            else:
                dp0[0] = 0
            for i in range(1, n):
                nd0 = [inf] * (k + 1)
                nd1 = [inf] * (k + 1)
                for c in range(k + 1):
                    nd0[c] = min(dp0[c], dp1[c])
                    if c:
                        nd1[c] = dp0[c - 1] + cost[i]
                dp0, dp1 = nd0, nd1
            return dp0[k] if first_taken else min(dp0[k], dp1[k])

        return min(solve(False), solve(True))
