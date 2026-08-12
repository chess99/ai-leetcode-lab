# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:22:47Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict, deque
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        words = set(wordList)
        if endWord not in words:
            return []
        words.add(beginWord)
        patterns = defaultdict(list)
        for word in words:
            for index in range(len(word)):
                patterns[word[:index] + '*' + word[index + 1:]].append(word)
        parent = {beginWord: None}
        queue = deque([beginWord])
        while queue:
            word = queue.popleft()
            if word == endWord:
                path = []
                while word is not None:
                    path.append(word)
                    word = parent[word]
                return path[::-1]
            for index in range(len(word)):
                key = word[:index] + '*' + word[index + 1:]
                for neighbor in patterns.pop(key, []):
                    if neighbor not in parent:
                        parent[neighbor] = word
                        queue.append(neighbor)
        return []
