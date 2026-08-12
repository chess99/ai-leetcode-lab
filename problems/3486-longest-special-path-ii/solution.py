# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        velontrida = (edges, nums)
        n = len(nums)
        graph = [[] for _ in range(n)]
        for u, v, length in edges:
            graph[u].append((v, length))
            graph[v].append((u, length))

        second_bit = [0] * (n + 1)
        third_bit = [0] * (n + 1)

        def add(bit, position, delta):
            index = position + 1
            while index <= n:
                bit[index] += delta
                index += index & -index

        def kth(bit, order):
            index = 0
            step = 1 << (n.bit_length() - 1)
            while step:
                nxt = index + step
                if nxt <= n and bit[nxt] < order:
                    order -= bit[nxt]
                    index = nxt
                step >>= 1
            return index

        occurrences = {}
        distance_path = []
        second_count = third_count = 0
        best_length = 0
        best_nodes = 1
        stack = [(0, -1, 0, True)]

        while stack:
            node, parent, distance, entering = stack.pop()
            value = nums[node]
            positions = occurrences.setdefault(value, [])
            if entering:
                old_second = positions[-2] if len(positions) >= 2 else None
                old_third = positions[-3] if len(positions) >= 3 else None
                if old_second is not None:
                    add(second_bit, old_second, -1)
                    second_count -= 1
                if old_third is not None:
                    add(third_bit, old_third, -1)
                    third_count -= 1

                depth = len(distance_path)
                positions.append(depth)
                distance_path.append(distance)
                if len(positions) >= 2:
                    add(second_bit, positions[-2], 1)
                    second_count += 1
                if len(positions) >= 3:
                    add(third_bit, positions[-3], 1)
                    third_count += 1

                second_largest = (kth(second_bit, second_count - 1)
                                  if second_count >= 2 else -1)
                largest_third = (kth(third_bit, third_count)
                                 if third_count else -1)
                left = max(second_largest, largest_third) + 1
                length = distance - distance_path[left]
                nodes = depth - left + 1
                if length > best_length or (length == best_length
                                             and nodes < best_nodes):
                    best_length = length
                    best_nodes = nodes

                stack.append((node, parent, distance, False))
                for child, weight in reversed(graph[node]):
                    if child != parent:
                        stack.append((child, node, distance + weight, True))
            else:
                old_second = positions[-2] if len(positions) >= 2 else None
                old_third = positions[-3] if len(positions) >= 3 else None
                if old_second is not None:
                    add(second_bit, old_second, -1)
                    second_count -= 1
                if old_third is not None:
                    add(third_bit, old_third, -1)
                    third_count -= 1
                positions.pop()
                distance_path.pop()
                if len(positions) >= 2:
                    add(second_bit, positions[-2], 1)
                    second_count += 1
                if len(positions) >= 3:
                    add(third_bit, positions[-3], 1)
                    third_count += 1

        return [best_length, best_nodes]
