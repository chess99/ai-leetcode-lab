# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        for row in boxGrid:
            write=len(row)-1
            for i in range(len(row)-1,-1,-1):
                if row[i]=='*':write=i-1
                elif row[i]=='#':row[i],row[write]=row[write],row[i];write-=1
        return [list(row) for row in zip(*boxGrid[::-1])]
