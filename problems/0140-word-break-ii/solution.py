# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        from functools import lru_cache
        words = set(wordDict); longest = max(map(len, words), default=0)
        @lru_cache(None)
        def split(start):
            if start == len(s): return [""]
            result = []
            for end in range(start + 1, min(len(s), start + longest) + 1):
                word = s[start:end]
                if word in words:
                    result += [word + (" " + tail if tail else "") for tail in split(end)]
            return result
        return split(0)
