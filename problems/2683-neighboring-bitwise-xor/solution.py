# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        value=0
        for x in derived: value^=x
        return value==0
