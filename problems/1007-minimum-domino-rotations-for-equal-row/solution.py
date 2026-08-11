# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:08:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def rotations(value):
            top=bottom=0
            for a,b in zip(tops,bottoms):
                if a!=value and b!=value:return float('inf')
                top+=a!=value;bottom+=b!=value
            return min(top,bottom)
        answer=min(rotations(tops[0]),rotations(bottoms[0]));return -1 if answer==float('inf') else answer
