# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:25Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        known=[set(items) for items in languages];need=set()
        for a,b in friendships:
            if not known[a-1]&known[b-1]:need|={a-1,b-1}
        return len(need)-max(Counter(language for person in need for language in known[person]).values(),default=0)
