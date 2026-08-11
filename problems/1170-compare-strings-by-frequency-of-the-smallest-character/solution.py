# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:26:23Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_right
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def frequency(word: str) -> int:
            smallest = min(word)
            return word.count(smallest)

        word_frequencies = sorted(frequency(word) for word in words)
        length = len(word_frequencies)
        return [length - bisect_right(word_frequencies, frequency(query))
                for query in queries]
