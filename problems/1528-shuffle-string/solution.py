# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:04:31Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result=['']*len(s)
        for char,index in zip(s,indices):result[index]=char
        return ''.join(result)
