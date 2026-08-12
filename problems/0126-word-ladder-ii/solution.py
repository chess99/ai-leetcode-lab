# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        from collections import defaultdict
        words = set(wordList)
        if endWord not in words: return []
        parents = defaultdict(set)
        level = {beginWord}
        while level and endWord not in parents:
            words -= level
            next_level = set()
            for word in level:
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        candidate = word[:i] + ch + word[i + 1:]
                        if candidate in words:
                            next_level.add(candidate); parents[candidate].add(word)
            level = next_level
        result = []
        def build(word, path):
            if word == beginWord: result.append(path[::-1]); return
            for parent in parents[word]: build(parent, path + [parent])
        if endWord in parents: build(endWord, [endWord])
        return result
