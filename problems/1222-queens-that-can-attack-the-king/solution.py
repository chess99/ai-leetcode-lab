# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:28:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        positions={tuple(q) for q in queens}; answer=[]
        for dr,dc in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
            r,c=king
            while 0<=r+dr<8 and 0<=c+dc<8:
                r+=dr;c+=dc
                if (r,c) in positions: answer.append([r,c]);break
        return answer
