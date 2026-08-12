# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:55Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def minPartitionScore(self, nums: List[int], k: int) -> int:
        pelunaxori = (nums, k)
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        n = len(nums)
        infinity = 10 ** 40
        previous = [infinity] * (n + 1)
        previous[0] = 0  # twice the real score

        def line(index: int):
            x = prefix[index]
            return -2 * x, previous[index] + x * x - x

        def value(item, x):
            return item[0] * x + item[1]

        def obsolete(first, second, third):
            return ((second[1] - first[1]) * (second[0] - third[0])
                    >= (third[1] - second[1]) * (first[0] - second[0]))

        for groups in range(1, k + 1):
            current = [infinity] * (n + 1)
            hull = deque([line(groups - 1)])
            for right in range(groups, n + 1):
                x = prefix[right]
                while len(hull) >= 2 and value(hull[0], x) >= value(hull[1], x):
                    hull.popleft()
                current[right] = x * x + x + value(hull[0], x)
                if previous[right] < infinity:
                    new_line = line(right)
                    while len(hull) >= 2 and obsolete(hull[-2], hull[-1], new_line):
                        hull.pop()
                    hull.append(new_line)
            previous = current
        return previous[n] // 2
