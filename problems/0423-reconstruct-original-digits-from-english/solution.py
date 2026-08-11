# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:03:16Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
class Solution:
    def originalDigits(self, s: str) -> str:
        counts=Counter(s); digits={0:('z','zero'),2:('w','two'),4:('u','four'),6:('x','six'),8:('g','eight'),3:('h','three'),5:('f','five'),7:('s','seven'),1:('o','one'),9:('i','nine')}; result=[]
        for digit,(key,word) in digits.items():
            number=counts[key]; result.extend(str(digit)*number)
            for c in word:counts[c]-=number
        return ''.join(sorted(result))
