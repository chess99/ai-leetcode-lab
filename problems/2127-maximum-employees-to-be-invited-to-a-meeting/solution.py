# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:10Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        size = len(favorite)
        indegree = [0] * size
        for person in favorite:
            indegree[person] += 1

        longest_chain = [1] * size
        queue = deque(index for index, degree in enumerate(indegree) if degree == 0)
        while queue:
            person = queue.popleft()
            target = favorite[person]
            longest_chain[target] = max(longest_chain[target],
                                        longest_chain[person] + 1)
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)

        largest_cycle = 0
        paired_chains = 0
        for start in range(size):
            if indegree[start] == 0:
                continue
            cycle = []
            person = start
            while indegree[person] > 0:
                cycle.append(person)
                indegree[person] = 0
                person = favorite[person]
            if len(cycle) == 2:
                paired_chains += (longest_chain[cycle[0]] +
                                  longest_chain[cycle[1]])
            else:
                largest_cycle = max(largest_cycle, len(cycle))

        return max(largest_cycle, paired_chains)
