# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:14Z
# Experiment: ai-leetcode-lab, round 1
class MapSum:

    def __init__(self):
        self.values = {}
        self.prefix_sums = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.values.get(key, 0)
        self.values[key] = val
        for end in range(1, len(key) + 1):
            prefix = key[:end]
            self.prefix_sums[prefix] = self.prefix_sums.get(prefix, 0) + delta

    def sum(self, prefix: str) -> int:
        return self.prefix_sums.get(prefix, 0)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
