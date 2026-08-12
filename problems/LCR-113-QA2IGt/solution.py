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
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1
        queue = deque(course for course in range(numCourses) if indegree[course] == 0)
        order = []
        while queue:
            course = queue.popleft()
            order.append(course)
            for following in graph[course]:
                indegree[following] -= 1
                if indegree[following] == 0:
                    queue.append(following)
        return order if len(order) == numCourses else []
