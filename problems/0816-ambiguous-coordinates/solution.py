# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:48:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def forms(part):
            if len(part) == 1: return [part]
            result = []
            if part[0] != '0': result.append(part)
            if part[-1] != '0':
                for i in range(1, len(part)):
                    if part[0] != '0' or i == 1: result.append(part[:i]+'.'+part[i:])
            return result
        digits=s[1:-1]; return [f'({x}, {y})' for i in range(1,len(digits)) for x in forms(digits[:i]) for y in forms(digits[i:])]
