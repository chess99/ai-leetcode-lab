# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:27Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        velnacqori = (l, r, k)

        def count_at_most(limit: int) -> int:
            if limit < 0:
                return 0
            low, high = 0, limit + 1
            while low + 1 < high:
                middle = (low + high) // 2
                if middle ** k <= limit:
                    low = middle
                else:
                    high = middle
            # 根 0..low 分别对应 low+1 个非负完全 k 次幂。
            return low + 1

        return count_at_most(velnacqori[1]) - count_at_most(velnacqori[0] - 1)
