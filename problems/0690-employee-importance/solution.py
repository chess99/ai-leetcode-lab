# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:31:05Z
# Experiment: ai-leetcode-lab, round 1
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
class Employee:
    def __init__(self, id, importance, subordinates):
        self.id, self.importance, self.subordinates = id, importance, subordinates
from typing import List


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        by_id = {employee.id: employee for employee in employees}
        total, stack = 0, [id]
        while stack:
            employee = by_id[stack.pop()]
            total += employee.importance
            stack.extend(employee.subordinates)
        return total
