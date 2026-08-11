# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:31:24Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        differences=[i for i in range(len(s1)) if s1[i]!=s2[i]]
        return not differences or len(differences)==2 and s1[differences[0]]==s2[differences[1]] and s1[differences[1]]==s2[differences[0]]
