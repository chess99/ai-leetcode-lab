# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        prefix = [0]
        for word in words:
            prefix.append(prefix[-1] + (word[0] in vowels and word[-1] in vowels))
        return [prefix[right + 1] - prefix[left] for left, right in queries]
