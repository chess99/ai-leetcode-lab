# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:52:35Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        need=0
        for value in data:
            if need:
                if value>>6!=2:return False
                need-=1
            elif value>>7==0: continue
            elif value>>5==6: need=1
            elif value>>4==14: need=2
            elif value>>3==30: need=3
            else:return False
        return need==0
