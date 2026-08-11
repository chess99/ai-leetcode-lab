# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:29:20Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        counts = Counter(s)
        target = len(s) // 4
        if all(counts[letter] == target for letter in "QWER"):
            return 0
        left = 0
        answer = len(s)
        for right, ch in enumerate(s):
            counts[ch] -= 1
            while all(counts[letter] <= target for letter in "QWER"):
                answer = min(answer, right - left + 1)
                counts[s[left]] += 1
                left += 1
        return answer
