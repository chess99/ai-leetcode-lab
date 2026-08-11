# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:09Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        values=[x for row in matrix for x in row];total=sum(map(abs,values));return total if sum(x<0 for x in values)%2==0 or 0 in values else total-2*min(map(abs,values))
