# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:25Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        size=len(encoded)+1;first=0
        for value in range(1,size+1):first^=value
        for index in range(1,len(encoded),2):first^=encoded[index]
        answer=[first]
        for value in encoded:answer.append(answer[-1]^value)
        return answer
