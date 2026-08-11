# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:25Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        first,second=Counter(a),Counter(b); answer=len(a)+len(b)
        for c in range(25):
            answer=min(answer,sum(first[chr(97+i)] for i in range(c+1,26))+sum(second[chr(97+i)] for i in range(c+1)),sum(second[chr(97+i)] for i in range(c+1,26))+sum(first[chr(97+i)] for i in range(c+1)))
        return min(answer,len(a)-max(first.values())+len(b)-max(second.values()))
