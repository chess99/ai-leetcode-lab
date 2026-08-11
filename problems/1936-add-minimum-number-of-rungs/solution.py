# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:06Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        previous=answer=0
        for rung in rungs:answer+=(rung-previous-1)//dist;previous=rung
        return answer
