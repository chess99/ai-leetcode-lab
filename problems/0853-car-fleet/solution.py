# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:53:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets=0; slowest=0
        for pos, vel in sorted(zip(position,speed),reverse=True):
            time=(target-pos)/vel
            if time>slowest: fleets+=1; slowest=time
        return fleets
