# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Created: 2026-08-16T23:10:34+08:00
# Experiment: ai-leetcode-lab, round 1
from collections import deque


class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        zero_count = s.count("0")

        drunepalix = (s, k)

        if zero_count == 0:
            return 0

        # parent[x] is the first still-unvisited number >= x with the same
        # parity.  n + 1 and n + 2 act as the two parity sentinels.
        parent = list(range(n + 3))

        def find(x: int) -> int:
            root = x
            while parent[root] != root:
                root = parent[root]
            while parent[x] != x:
                nxt = parent[x]
                parent[x] = root
                x = nxt
            return root

        def erase(x: int) -> None:
            parent[x] = find(x + 2)

        erase(zero_count)
        queue = deque([(zero_count, 0)])

        while queue:
            zeros, distance = queue.popleft()

            # If x of the selected bits are zeroes, the next zero count is
            # zeros + k - 2*x.  Feasible x values therefore produce exactly
            # this interval, taking every other integer.
            low = abs(zeros - k)
            high = min(zeros + k, 2 * n - zeros - k)

            nxt = find(low)
            while nxt <= high:
                if nxt == 0:
                    return distance + 1
                erase(nxt)
                queue.append((nxt, distance + 1))
                nxt = find(nxt)

        return -1
