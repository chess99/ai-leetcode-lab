# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:27Z
# Experiment: ai-leetcode-lab, round 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        row = 0
        col = 0

        while head is not None:
            matrix[row][col] = head.val
            head = head.next

            row_change, col_change = directions[direction]
            next_row = row + row_change
            next_col = col + col_change

            if not (
                0 <= next_row < m
                and 0 <= next_col < n
                and matrix[next_row][next_col] == -1
            ):
                direction = (direction + 1) % 4
                row_change, col_change = directions[direction]
                next_row = row + row_change
                next_col = col + col_change

            row, col = next_row, next_col

        return matrix
