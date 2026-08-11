# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:33Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        return [sum((x-a)**2+(y-b)**2<=r*r for x,y in points) for a,b,r in queries]
