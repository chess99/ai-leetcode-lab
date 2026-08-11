# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:30:44Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class MagicDictionary:

    def __init__(self):
        self.patterns = defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for index, char in enumerate(word):
                self.patterns[word[:index] + "*" + word[index + 1 :]].add(char)

    def search(self, searchWord: str) -> bool:
        for index, char in enumerate(searchWord):
            candidates = self.patterns[searchWord[:index] + "*" + searchWord[index + 1 :]]
            if any(candidate != char for candidate in candidates):
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
