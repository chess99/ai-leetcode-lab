# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:59Z
# Experiment: ai-leetcode-lab, round 1
class WordsFrequency:

    def __init__(self, book: List[str]):
        from collections import Counter
        self.counts = Counter(book)

    def get(self, word: str) -> int:
        return self.counts[word]


# Your WordsFrequency object will be instantiated and called as such:
# obj = WordsFrequency(book)
# param_1 = obj.get(word)
