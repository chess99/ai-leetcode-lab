# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:23:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        counts={}
        for value in range(lowLimit,highLimit+1):
            box=sum(map(int,str(value))); counts[box]=counts.get(box,0)+1
        return max(counts.values())
