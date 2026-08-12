# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:01Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        text=str(n);d=set(digits);answer=sum(len(digits)**i for i in range(1,len(text)))
        for i,ch in enumerate(text):
            answer+=sum(x<ch for x in digits)*len(digits)**(len(text)-i-1)
            if ch not in d:return answer
        return answer+1
