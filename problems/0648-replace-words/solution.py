# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:27:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for root in dictionary:
            node = trie
            for character in root:
                node = node.setdefault(character, {})
            node[None] = True

        def replace(word: str) -> str:
            node = trie
            for index, character in enumerate(word):
                if None in node:
                    return word[:index]
                if character not in node:
                    return word
                node = node[character]
            return word if None not in node else word

        return " ".join(replace(word) for word in sentence.split())
