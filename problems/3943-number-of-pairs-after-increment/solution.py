# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-13T00:00:00Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left, bisect_right
from collections import Counter


class Solution:
    def numberOfPairs(
        self,
        nums1: list[int],
        nums2: list[int],
        queries: list[list[int]],
    ) -> list[int]:
        zenthurapi = (nums1, nums2, queries)
        count1 = Counter(zenthurapi[0])
        values = zenthurapi[1][:]
        n = len(values)
        block_size = 450
        block_count = (n + block_size - 1) // block_size
        lazy = [0] * block_count
        ordered = [
            sorted(values[b * block_size : min(n, (b + 1) * block_size)])
            for b in range(block_count)
        ]

        def rebuild(block: int) -> None:
            start = block * block_size
            end = min(n, start + block_size)
            if lazy[block]:
                increment = lazy[block]
                for i in range(start, end):
                    values[i] += increment
                lazy[block] = 0
            ordered[block] = sorted(values[start:end])

        def partial_update(block: int, left: int, right: int, increment: int) -> None:
            rebuild(block)
            for i in range(left, right + 1):
                values[i] += increment
            start = block * block_size
            end = min(n, start + block_size)
            ordered[block] = sorted(values[start:end])

        def frequency(target: int) -> int:
            total = 0
            for block in range(block_count):
                wanted = target - lazy[block]
                data = ordered[block]
                total += bisect_right(data, wanted) - bisect_left(data, wanted)
            return total

        answer = []
        for query in zenthurapi[2]:
            if query[0] == 1:
                _, left, right, increment = query
                left_block = left // block_size
                right_block = right // block_size
                if left_block == right_block:
                    block_start = left_block * block_size
                    block_end = min(n, block_start + block_size) - 1
                    if left == block_start and right == block_end:
                        lazy[left_block] += increment
                    else:
                        partial_update(left_block, left, right, increment)
                    continue

                left_end = min(n, (left_block + 1) * block_size) - 1
                if left == left_block * block_size:
                    lazy[left_block] += increment
                else:
                    partial_update(left_block, left, left_end, increment)

                right_start = right_block * block_size
                right_end = min(n, right_start + block_size) - 1
                if right == right_end:
                    lazy[right_block] += increment
                else:
                    partial_update(right_block, right_start, right, increment)

                for block in range(left_block + 1, right_block):
                    lazy[block] += increment
            else:
                total = query[1]
                pairs = 0
                for value, multiplicity in count1.items():
                    pairs += multiplicity * frequency(total - value)
                answer.append(pairs)

        return answer
