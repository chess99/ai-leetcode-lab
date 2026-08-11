# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:52:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reachable = [[False] * numCourses for _ in range(numCourses)]
        for source, target in prerequisites:
            reachable[source][target] = True
        for middle in range(numCourses):
            for source in range(numCourses):
                if reachable[source][middle]:
                    for target in range(numCourses):
                        reachable[source][target] |= reachable[middle][target]
        return [reachable[source][target] for source, target in queries]
