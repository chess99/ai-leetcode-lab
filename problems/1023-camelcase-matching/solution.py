# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:10:49Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def matches(query):
            i=0
            for char in query:
                if i<len(pattern) and char==pattern[i]:i+=1
                elif char.isupper():return False
            return i==len(pattern)
        return [matches(query) for query in queries]
