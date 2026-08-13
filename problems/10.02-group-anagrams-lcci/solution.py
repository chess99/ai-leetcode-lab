# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        groups = defaultdict(list)
        for word in strs:
            groups["".join(sorted(word))].append(word)
        return list(groups.values())
