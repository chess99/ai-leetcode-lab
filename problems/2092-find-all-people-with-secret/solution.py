# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:08Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        known = {0, firstPerson}
        meetings.sort(key=lambda meeting: meeting[2])
        index = 0
        while index < len(meetings):
            end = index
            graph = defaultdict(list)
            participants = set()
            while end < len(meetings) and meetings[end][2] == meetings[index][2]:
                first, second, _ = meetings[end]
                graph[first].append(second)
                graph[second].append(first)
                participants.update((first, second))
                end += 1
            queue = deque(participants & known)
            reached = set(queue)
            while queue:
                person = queue.popleft()
                for neighbor in graph[person]:
                    if neighbor not in reached:
                        reached.add(neighbor)
                        queue.append(neighbor)
            known.update(reached)
            index = end
        return list(known)
