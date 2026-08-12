# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:24:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        index = 0
        while index < len(words):
            start = index
            letters = 0
            while index < len(words) and letters + len(words[index]) + index - start <= maxWidth:
                letters += len(words[index])
                index += 1
            count = index - start
            if index == len(words) or count == 1:
                line = " ".join(words[start:index])
                result.append(line + " " * (maxWidth - len(line)))
                continue
            spaces, extra = divmod(maxWidth - letters, count - 1)
            line = ""
            for offset in range(count - 1):
                line += words[start + offset] + " " * (spaces + (offset < extra))
            result.append(line + words[index - 1])
        return result
