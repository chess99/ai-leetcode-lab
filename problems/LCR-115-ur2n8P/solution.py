# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:28Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        graph = {value: set() for value in nums}
        indegree = {value: 0 for value in nums}
        seen = set()
        for sequence in sequences:
            for value in sequence:
                if value not in graph:
                    return False
                seen.add(value)
            for previous, current in zip(sequence, sequence[1:]):
                if current not in graph[previous]:
                    graph[previous].add(current)
                    indegree[current] += 1
        if len(seen) != len(nums):
            return False
        queue = deque(value for value in nums if indegree[value] == 0)
        index = 0
        while queue:
            if len(queue) != 1:
                return False
            value = queue.popleft()
            if index >= len(nums) or value != nums[index]:
                return False
            index += 1
            for following in graph[value]:
                indegree[following] -= 1
                if indegree[following] == 0:
                    queue.append(following)
        return index == len(nums)
