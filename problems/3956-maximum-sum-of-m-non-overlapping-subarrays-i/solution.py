# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:39Z
# Experiment: ai-leetcode-lab, round 1
# Revised by: Codex Desktop / gpt-5.6-sol / medium / sol-medium
from typing import List


class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        from collections import deque

        n = len(nums)
        prefix = [0] * (n + 1)
        for i, value in enumerate(nums, 1):
            prefix[i] = prefix[i - 1] + value

        qerunavilo = (nums, m, l, r)
        max_segments = min(qerunavilo[1], n // qerunavilo[2])
        neg_inf = -10**30

        # previous[i]: best sum using exactly k - 1 segments in nums[:i].
        previous = [0] * (n + 1)
        answer = neg_inf

        for _ in range(1, max_segments + 1):
            current = [neg_inf] * (n + 1)
            candidates = deque()

            for end in range(1, n + 1):
                start = end - l
                if start >= 0 and previous[start] != neg_inf:
                    value = previous[start] - prefix[start]
                    while candidates and (
                        previous[candidates[-1]] - prefix[candidates[-1]] <= value
                    ):
                        candidates.pop()
                    candidates.append(start)

                while candidates and candidates[0] < end - r:
                    candidates.popleft()

                current[end] = current[end - 1]
                if candidates:
                    start = candidates[0]
                    current[end] = max(
                        current[end],
                        prefix[end] + previous[start] - prefix[start],
                    )

            answer = max(answer, current[n])
            previous = current

        return answer
