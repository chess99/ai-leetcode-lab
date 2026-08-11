# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:17Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        left = answer = 0
        for right, char in enumerate(s):
            counts[char] += 1
            while counts[char] >= k:
                answer += len(s) - right
                counts[s[left]] -= 1
                left += 1
        return answer
