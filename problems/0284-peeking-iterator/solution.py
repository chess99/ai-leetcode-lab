# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:44:32Z
# Experiment: ai-leetcode-lab, round 1
class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.cached = None
        self.has_cached = False

    def peek(self) -> int:
        if not self.has_cached:
            self.cached = self.iterator.next()
            self.has_cached = True
        return self.cached

    def next(self) -> int:
        if self.has_cached:
            self.has_cached = False
            return self.cached
        return self.iterator.next()

    def hasNext(self) -> bool:
        return self.has_cached or self.iterator.hasNext()
