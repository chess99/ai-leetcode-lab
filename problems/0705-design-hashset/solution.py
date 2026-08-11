# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:04:51Z
# Experiment: ai-leetcode-lab, round 1
class MyHashSet:

    def __init__(self):
        self.values=set()

    def add(self, key: int) -> None:
        self.values.add(key)

    def remove(self, key: int) -> None:
        self.values.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.values


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
