# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:59:15Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        positions={}
        for index,char in enumerate(s):
            if char in positions:
                if index-positions[char]-1 != distance[ord(char)-97]:return False
            else:positions[char]=index
        return True
