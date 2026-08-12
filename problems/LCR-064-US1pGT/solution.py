# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class MagicDictionary:

    def __init__(self):
        self.words_by_length = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.words_by_length.setdefault(len(word), []).append(word)

    def search(self, searchWord: str) -> bool:
        for word in self.words_by_length.get(len(searchWord), []):
            differences = 0
            for left, right in zip(word, searchWord):
                if left != right:
                    differences += 1
                    if differences > 1:
                        break
            if differences == 1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
