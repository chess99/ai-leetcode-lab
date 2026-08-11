# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:48:11Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        return (ord(coordinate1[0])+int(coordinate1[1]))%2 == (ord(coordinate2[0])+int(coordinate2[1]))%2
