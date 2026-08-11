# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:32:49Z
# Experiment: ai-leetcode-lab, round 1
class _WordNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = _WordNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children.setdefault(char, _WordNode())
        node.is_word = True

    def search(self, word: str) -> bool:
        def matches(index: int, node: _WordNode) -> bool:
            if index == len(word):
                return node.is_word
            char = word[index]
            if char == ".":
                return any(matches(index + 1, child) for child in node.children.values())
            return char in node.children and matches(index + 1, node.children[char])

        return matches(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
