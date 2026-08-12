# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:24:52Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter, defaultdict
        if not words:
            return []
        width = len(words[0])
        needed = Counter(words)
        answer = []
        for offset in range(width):
            left = offset
            count = 0
            window = defaultdict(int)
            for right in range(offset, len(s) - width + 1, width):
                word = s[right:right + width]
                if word not in needed:
                    window.clear()
                    count = 0
                    left = right + width
                    continue
                window[word] += 1
                count += 1
                while window[word] > needed[word]:
                    removed = s[left:left + width]
                    window[removed] -= 1
                    count -= 1
                    left += width
                if count == len(words):
                    answer.append(left)
                    removed = s[left:left + width]
                    window[removed] -= 1
                    count -= 1
                    left += width
        return answer
