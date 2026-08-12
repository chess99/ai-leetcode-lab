# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        remaining = set(wordList)
        if endWord not in remaining:
            return 0
        front = {beginWord}
        back = {endWord}
        remaining.discard(beginWord)
        length = 1
        while front:
            if len(front) > len(back):
                front, back = back, front
            nxt = set()
            for word in front:
                chars = list(word)
                for index, original in enumerate(chars):
                    for code in range(97, 123):
                        char = chr(code)
                        if char == original:
                            continue
                        chars[index] = char
                        candidate = ''.join(chars)
                        if candidate in back:
                            return length + 1
                        if candidate in remaining:
                            remaining.remove(candidate)
                            nxt.add(candidate)
                    chars[index] = original
            front = nxt
            length += 1
        return 0
