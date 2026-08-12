# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:51Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        counts=Counter(digits);remainder=sum(digits)%3
        def remove(candidates,amount):
            for digit in candidates:
                take=min(counts[digit],amount);counts[digit]-=take;amount-=take
                if amount==0:return True
            return False
        if remainder==1:
            if not remove((1,4,7),1):remove((2,5,8),2)
        elif remainder==2:
            if not remove((2,5,8),1):remove((1,4,7),2)
        answer=''.join(str(digit)*counts[digit] for digit in range(9,-1,-1))
        return '0' if answer and answer[0]=='0' else answer
