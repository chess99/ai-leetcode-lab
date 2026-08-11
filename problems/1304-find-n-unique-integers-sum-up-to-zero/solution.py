# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:46:01Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def sumZero(self, n: int) -> List[int]:
        result=list(range(1,n//2+1)); return result+[-value for value in result]+([0] if n%2 else [])
