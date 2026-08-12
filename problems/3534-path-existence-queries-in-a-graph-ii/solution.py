# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:19Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_right
from typing import List


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        ordered = sorted((value, index) for index, value in enumerate(nums))
        values = [value for value, _ in ordered]
        rank = [0] * n
        for position, (_, original) in enumerate(ordered):
            rank[original] = position

        component = [0] * n
        for position in range(1, n):
            component[position] = component[position - 1]
            if values[position] - values[position - 1] > maxDiff:
                component[position] += 1

        first_jump = [bisect_right(values, value + maxDiff) - 1
                      for value in values]
        jumps = [first_jump]
        while (1 << len(jumps)) <= n:
            previous = jumps[-1]
            jumps.append([previous[previous[i]] for i in range(n)])

        answer = []
        for u, v in queries:
            left, right = rank[u], rank[v]
            if left == right:
                answer.append(0)
                continue
            if left > right:
                left, right = right, left
            if component[left] != component[right]:
                answer.append(-1)
                continue
            distance = 0
            current = left
            for level in range(len(jumps) - 1, -1, -1):
                nxt = jumps[level][current]
                if nxt < right:
                    current = nxt
                    distance += 1 << level
            answer.append(distance + 1)
        return answer
