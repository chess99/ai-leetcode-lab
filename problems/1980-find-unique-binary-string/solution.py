# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:10Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return ''.join('1' if value[i]=='0' else '0' for i,value in enumerate(nums))
