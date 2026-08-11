# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:25Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        values=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j]^=(matrix[i-1][j] if i else 0)^(matrix[i][j-1] if j else 0)^(matrix[i-1][j-1] if i and j else 0);values.append(matrix[i][j])
        return sorted(values,reverse=True)[k-1]
