# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:42:08Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0,y0=coordinates[0]; dx=coordinates[1][0]-x0; dy=coordinates[1][1]-y0
        return all((x-x0)*dy == (y-y0)*dx for x,y in coordinates[2:])
