# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        def matches(text):
            pi = [0] * len(pattern)
            for i in range(1, len(pattern)):
                j = pi[i - 1]
                while j and pattern[i] != pattern[j]:
                    j = pi[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                pi[i] = j
            starts = []
            j = 0
            for i, char in enumerate(text):
                while j and char != pattern[j]:
                    j = pi[j - 1]
                if char == pattern[j]:
                    j += 1
                if j == len(pattern):
                    starts.append(i - len(pattern) + 1)
                    j = pi[j - 1]
            return starts

        rows, cols = len(grid), len(grid[0])
        total = rows * cols
        horizontal = [cell for row in grid for cell in row]
        vertical = [grid[r][c] for c in range(cols) for r in range(rows)]
        hdiff = [0] * (total + 1)
        vdiff = [0] * (total + 1)
        length = len(pattern)
        for start in matches(horizontal):
            hdiff[start] += 1
            hdiff[start + length] -= 1
        for start in matches(vertical):
            vdiff[start] += 1
            vdiff[start + length] -= 1
        answer = 0
        hactive = 0
        vactive = [0] * total
        for i in range(total):
            hactive += hdiff[i]
            vactive[i] = (vactive[i - 1] if i else 0) + vdiff[i]
        hactive = 0
        for index in range(total):
            hactive += hdiff[index]
            r, c = divmod(index, cols)
            if hactive and vactive[c * rows + r]:
                answer += 1
        return answer
