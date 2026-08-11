# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        score=0
        for turn,index in enumerate(sorted(range(len(aliceValues)),key=lambda i:aliceValues[i]+bobValues[i],reverse=True)):
            score+=aliceValues[index] if turn%2==0 else -bobValues[index]
        return (score>0)-(score<0)
