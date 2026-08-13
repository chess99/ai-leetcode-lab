# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-13T00:00:00Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque


class Solution:
    def maximumSum(self, nums: list[int], m: int, l: int, r: int) -> int:
        fentoluric = (nums, m, l, r)
        nums, m, l, r = fentoluric
        n = len(nums)
        m = min(m, n // l)

        prefix = [0] * (n + 1)
        for i, value in enumerate(nums, 1):
            prefix[i] = prefix[i - 1] + value

        def penalized(penalty: int) -> tuple[int, int]:
            # Lexicographically maximize (sum - penalty * segments, segments).
            best_score = [0] * (n + 1)
            best_count = [0] * (n + 1)
            candidates: deque[tuple[tuple[int, int], int]] = deque()

            for end in range(1, n + 1):
                start = end - l
                if start >= 0:
                    key = (
                        best_score[start] - prefix[start],
                        best_count[start],
                    )
                    while candidates and candidates[-1][0] <= key:
                        candidates.pop()
                    candidates.append((key, start))

                while candidates and candidates[0][1] < end - r:
                    candidates.popleft()

                best_score[end] = best_score[end - 1]
                best_count[end] = best_count[end - 1]
                if candidates:
                    key = candidates[0][0]
                    take = (key[0] + prefix[end] - penalty, key[1] + 1)
                    skip = (best_score[end], best_count[end])
                    if take > skip:
                        best_score[end], best_count[end] = take

            return best_score[n], best_count[n]

        unrestricted_score, unrestricted_count = penalized(0)
        if unrestricted_count == 0:
            # The DP may select no segment, but the statement requires one.
            best_one = -10**30
            candidates: deque[int] = deque()
            for end in range(1, n + 1):
                start = end - l
                if start >= 0:
                    while candidates and prefix[candidates[-1]] >= prefix[start]:
                        candidates.pop()
                    candidates.append(start)
                while candidates and candidates[0] < end - r:
                    candidates.popleft()
                if candidates:
                    best_one = max(best_one, prefix[end] - prefix[candidates[0]])
            return best_one

        if unrestricted_count <= m:
            return unrestricted_score

        low = 0
        high = sum(abs(value) for value in nums) + 1
        while low + 1 < high:
            penalty = (low + high) // 2
            if penalized(penalty)[1] >= m:
                low = penalty
            else:
                high = penalty

        score, _ = penalized(low)
        return score + low * m
