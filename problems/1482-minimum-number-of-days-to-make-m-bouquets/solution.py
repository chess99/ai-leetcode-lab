# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:53:32Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):return -1
        def enough(day):
            bouquets=flowers=0
            for bloom in bloomDay:
                if bloom<=day:
                    flowers+=1
                    if flowers==k:bouquets+=1;flowers=0
                else:flowers=0
            return bouquets>=m
        left,right=min(bloomDay),max(bloomDay)
        while left<right:
            middle=(left+right)//2
            if enough(middle):right=middle
            else:left=middle+1
        return left
