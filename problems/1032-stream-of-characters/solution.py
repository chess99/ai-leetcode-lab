# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:07Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class StreamChecker:

    def __init__(self, words: List[str]):
        self.children = [{}]
        self.failure = [0]
        self.terminal = [False]
        for word in words:
            node = 0
            for char in word:
                if char not in self.children[node]:
                    self.children[node][char] = len(self.children)
                    self.children.append({})
                    self.failure.append(0)
                    self.terminal.append(False)
                node = self.children[node][char]
            self.terminal[node] = True
        queue = deque(self.children[0].values())
        while queue:
            node = queue.popleft()
            self.terminal[node] |= self.terminal[self.failure[node]]
            for char, following in self.children[node].items():
                fallback = self.failure[node]
                while fallback and char not in self.children[fallback]:
                    fallback = self.failure[fallback]
                self.failure[following] = self.children[fallback].get(char, 0)
                queue.append(following)
        self.state = 0

    def query(self, letter: str) -> bool:
        while self.state and letter not in self.children[self.state]:
            self.state = self.failure[self.state]
        self.state = self.children[self.state].get(letter, 0)
        return self.terminal[self.state]


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
