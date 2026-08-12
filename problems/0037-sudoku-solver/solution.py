# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:24:52Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9
        columns = [0] * 9
        boxes = [0] * 9
        empty = []
        for row in range(9):
            for column in range(9):
                if board[row][column] == '.':
                    empty.append((row, column))
                else:
                    bit = 1 << (ord(board[row][column]) - ord('1'))
                    rows[row] |= bit
                    columns[column] |= bit
                    boxes[row // 3 * 3 + column // 3] |= bit

        def search(position: int) -> bool:
            if position == len(empty):
                return True
            best = position
            best_mask = 0
            best_count = 10
            for index in range(position, len(empty)):
                row, column = empty[index]
                box = row // 3 * 3 + column // 3
                mask = 0x1FF & ~(rows[row] | columns[column] | boxes[box])
                count = mask.bit_count()
                if count < best_count:
                    best, best_mask, best_count = index, mask, count
                    if count <= 1:
                        break
            if best_count == 0:
                return False
            empty[position], empty[best] = empty[best], empty[position]
            row, column = empty[position]
            box = row // 3 * 3 + column // 3
            mask = best_mask
            while mask:
                bit = mask & -mask
                mask -= bit
                rows[row] |= bit
                columns[column] |= bit
                boxes[box] |= bit
                board[row][column] = str(bit.bit_length())
                if search(position + 1):
                    return True
                rows[row] ^= bit
                columns[column] ^= bit
                boxes[box] ^= bit
            board[row][column] = '.'
            empty[position], empty[best] = empty[best], empty[position]
            return False

        search(0)
