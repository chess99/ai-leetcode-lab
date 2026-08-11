# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:25Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        total = Counter(s)
        if any(total[c] < k for c in 'abc'):
            return -1
        window = Counter()
        left = best = 0
        for right, ch in enumerate(s):
            window[ch] += 1
            while total[ch] - window[ch] < k:
                window[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return len(s) - best
