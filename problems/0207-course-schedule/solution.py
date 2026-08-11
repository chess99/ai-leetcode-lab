# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:32:48Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            degree[course] += 1
        queue = deque(i for i in range(numCourses) if degree[i] == 0)
        completed = 0
        while queue:
            course = queue.popleft()
            completed += 1
            for next_course in graph[course]:
                degree[next_course] -= 1
                if degree[next_course] == 0:
                    queue.append(next_course)
        return completed == numCourses
