# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:16:17Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a,b,c=points
        return (b[0]-a[0])*(c[1]-a[1]) != (b[1]-a[1])*(c[0]-a[0])
