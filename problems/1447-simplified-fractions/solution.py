# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:51:29Z
# Experiment: ai-leetcode-lab, round 1
from math import gcd
from typing import List
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        return [f'{top}/{bottom}' for bottom in range(2,n+1) for top in range(1,bottom) if gcd(top,bottom)==1]
