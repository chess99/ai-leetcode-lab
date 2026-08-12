# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:43Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.encoding = dict(zip(keys, values))
        encrypted_dictionary = []
        for word in dictionary:
            encrypted = self.encrypt(word)
            if encrypted:
                encrypted_dictionary.append(encrypted)
        self.frequencies = Counter(encrypted_dictionary)

    def encrypt(self, word1: str) -> str:
        pieces = []
        for character in word1:
            if character not in self.encoding:
                return ""
            pieces.append(self.encoding[character])
        return "".join(pieces)

    def decrypt(self, word2: str) -> int:
        return self.frequencies[word2]


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
