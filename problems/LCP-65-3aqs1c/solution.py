# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Revised by: Codex Desktop / gpt-5.6-sol / medium / sol-medium
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def unSuitability(self, operate: List[int]) -> int:
        # 状态 u 表示当前前缀和到历史最小前缀和的距离；dp[u] 是在
        # 该状态下能够达到的最小历史极差。
        bound = 2 * max(operate)
        inf = bound + 1
        dp = [inf] * (bound + 1)
        dp[0] = 0

        for x in operate:
            ndp = [inf] * (bound + 1)
            for u, width in enumerate(dp):
                if width > bound:
                    continue

                # 给 x 取正号。
                nu = u + x
                if nu <= bound:
                    nw = width if nu <= width else nu
                    if nw < ndp[nu]:
                        ndp[nu] = nw

                # 给 x 取负号。
                if x <= u:
                    nu = u - x
                    nw = width
                else:
                    nu = 0
                    nw = width + x - u
                if nw <= bound and nw < ndp[nu]:
                    ndp[nu] = nw
            dp = ndp

        return min(dp)
