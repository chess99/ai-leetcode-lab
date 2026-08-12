# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:16:00Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_right
from typing import List


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        coordinates = sorted({0} | {query[1] for query in queries if query[0] == 1})
        count = len(coordinates)
        rank = {value: index for index, value in enumerate(coordinates)}

        size = 1
        while size < count:
            size <<= 1
        tree = [0] * (2 * size)
        for index in range(1, count):
            tree[size + index] = coordinates[index] - coordinates[index - 1]
        for index in range(size - 1, 0, -1):
            tree[index] = max(tree[index << 1], tree[index << 1 | 1])

        def update(index, value):
            index += size
            tree[index] = value
            index >>= 1
            while index:
                tree[index] = max(tree[index << 1], tree[index << 1 | 1])
                index >>= 1

        def prefix_max(end):
            left = size
            right = size + end
            result = 0
            while left < right:
                if left & 1:
                    result = max(result, tree[left])
                    left += 1
                if right & 1:
                    right -= 1
                    result = max(result, tree[right])
                left >>= 1
                right >>= 1
            return result

        previous = [index - 1 for index in range(count)]
        following = [index + 1 for index in range(count)]
        following[-1] = count
        predecessor_parent = list(range(count))

        def find(index):
            while index != predecessor_parent[index]:
                predecessor_parent[index] = predecessor_parent[predecessor_parent[index]]
                index = predecessor_parent[index]
            return index

        reversed_answer = []
        for query in reversed(queries):
            if query[0] == 2:
                _, right_endpoint, block_size = query
                bound = bisect_right(coordinates, right_endpoint)
                predecessor = find(bound - 1)
                longest = max(prefix_max(bound),
                              right_endpoint - coordinates[predecessor])
                reversed_answer.append(longest >= block_size)
            else:
                index = rank[query[1]]
                left_index = previous[index]
                right_index = following[index]
                update(index, 0)
                if right_index < count:
                    update(right_index,
                           coordinates[right_index] - coordinates[left_index])
                    previous[right_index] = left_index
                following[left_index] = right_index
                predecessor_parent[index] = find(index - 1)

        return reversed_answer[::-1]
