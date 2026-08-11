# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:50:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        result=1
        for digit in b: result=pow(result,10,1337)*pow(a,digit,1337)%1337
        return result
