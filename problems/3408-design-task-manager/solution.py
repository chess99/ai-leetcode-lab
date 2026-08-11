# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:17Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = {}
        self.heap = []
        for user, task, priority in tasks:
            self.add(user, task, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        user, _ = self.tasks[taskId]
        self.add(user, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        del self.tasks[taskId]

    def execTop(self) -> int:
        while self.heap:
            neg_priority, neg_task, user = heapq.heappop(self.heap)
            task, priority = -neg_task, -neg_priority
            if self.tasks.get(task) == (user, priority):
                del self.tasks[task]
                return user
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
