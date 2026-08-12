# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:16Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        relominexa = (s, queries)
        prefix_ones = [0]
        for char in s:
            prefix_ones.append(prefix_ones[-1] + (char == '1'))

        starts = []
        ends = []
        lengths = []
        index = 0
        while index < len(s):
            if s[index] == '1':
                index += 1
                continue
            end = index
            while end + 1 < len(s) and s[end + 1] == '0':
                end += 1
            starts.append(index)
            ends.append(end)
            lengths.append(end - index + 1)
            index = end + 1

        pair_count = max(0, len(lengths) - 1)
        size = 1
        while size < pair_count:
            size <<= 1
        tree = [0] * (2 * size)
        for i in range(pair_count):
            tree[size + i] = lengths[i] + lengths[i + 1]
        for node in range(size - 1, 0, -1):
            tree[node] = max(tree[node * 2], tree[node * 2 + 1])

        def range_max(left: int, right: int) -> int:
            """Maximum pair value for inclusive pair-index range."""
            if left > right:
                return 0
            left += size
            right += size + 1
            result = 0
            while left < right:
                if left & 1:
                    result = max(result, tree[left])
                    left += 1
                if right & 1:
                    right -= 1
                    result = max(result, tree[right])
                left //= 2
                right //= 2
            return result

        answer = []
        for left, right in relominexa[1]:
            ones = prefix_ones[-1]
            first = bisect_left(ends, left)
            last = bisect_right(starts, right) - 1
            gain = 0
            if first < last:
                first_length = ends[first] - max(left, starts[first]) + 1
                last_length = min(right, ends[last]) - starts[last] + 1
                if first + 1 == last:
                    gain = first_length + last_length
                else:
                    gain = max(
                        first_length + lengths[first + 1],
                        lengths[last - 1] + last_length,
                        range_max(first + 1, last - 2),
                    )
            answer.append(ones + gain)
        return answer
