# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: ultra
# Profile: sol-ultra
# Created: 2026-08-12T17:58:49Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def ringGame(self, challenge: List[int]) -> int:
        n = len(challenge)

        def can_win(initial: int) -> bool:
            parent = list(range(n))
            size = [1] * n
            value_or = challenge.copy()
            left = list(range(n))
            right = list(range(n))
            active = [False] * n

            def find(x: int) -> int:
                while parent[x] != x:
                    parent[x] = parent[parent[x]]
                    x = parent[x]
                return x

            def union(x: int, y: int) -> int:
                x = find(x)
                y = find(y)
                if x == y:
                    return x
                if size[x] < size[y]:
                    x, y = y, x
                parent[y] = x
                size[x] += size[y]
                value_or[x] |= value_or[y]
                return x

            for i, value in enumerate(challenge):
                active[i] = value <= initial

            # 先把所有相邻的可行单点缩成极大的连续区间。
            for i in range(n - 1):
                if active[i] and active[i + 1]:
                    x = find(i)
                    y = find(i + 1)
                    new_left = left[x]
                    new_right = right[y]
                    root = union(x, y)
                    left[root] = new_left
                    right[root] = new_right

            if n > 1 and active[0] and active[n - 1]:
                x = find(n - 1)
                y = find(0)
                if x != y:
                    new_left = left[x]
                    new_right = right[y]
                    root = union(x, y)
                    left[root] = new_left
                    right[root] = new_right

            queue = deque({find(i) for i in range(n) if active[i]})

            def absorb(root: int, index: int, from_left: bool) -> int:
                """把一个边界点吸入 root，并顺便合并它另一侧的活动区间。"""
                root = find(root)
                active[index] = True
                old_left = left[root]
                old_right = right[root]
                root = union(root, index)
                if from_left:
                    left[root] = index
                    right[root] = old_right
                    neighbour = (index - 1) % n
                else:
                    left[root] = old_left
                    right[root] = index
                    neighbour = (index + 1) % n

                if active[neighbour]:
                    other = find(neighbour)
                    root = find(root)
                    if other != root:
                        if from_left:
                            new_left = left[other]
                            new_right = right[root]
                        else:
                            new_left = left[root]
                            new_right = right[other]
                        root = union(root, other)
                        left[root] = new_left
                        right[root] = new_right
                return root

            while queue:
                root = find(queue.popleft())
                if size[root] == n:
                    return True

                score = initial | value_or[root]
                index = (left[root] - 1) % n
                if not active[index] and challenge[index] <= score:
                    queue.append(absorb(root, index, True))
                    continue

                index = (right[root] + 1) % n
                if not active[index] and challenge[index] <= score:
                    queue.append(absorb(root, index, False))

            return False

        # 数值二分不适用：OR 对普通数值大小并不单调。逐位贪心时，
        # candidate 是当前前缀下能取得的最大值；若它仍不可行，该位必须为 1。
        answer = 0
        for bit in range(max(challenge).bit_length() - 1, -1, -1):
            candidate = answer | ((1 << bit) - 1)
            if not can_win(candidate):
                answer |= 1 << bit
        return answer
