# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:59:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findString(self, words: List[str], s: str) -> int:
        left, right = 0, len(words) - 1
        while left <= right:
            middle = (left + right) // 2
            probe_left = probe_right = middle
            while probe_left >= left or probe_right <= right:
                if probe_left >= left and words[probe_left]:
                    middle = probe_left
                    break
                if probe_right <= right and words[probe_right]:
                    middle = probe_right
                    break
                probe_left -= 1
                probe_right += 1
            else:
                return -1

            if words[middle] == s:
                return middle
            if words[middle] < s:
                left = middle + 1
            else:
                right = middle - 1
        return -1
