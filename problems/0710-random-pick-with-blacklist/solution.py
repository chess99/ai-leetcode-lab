# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:47Z
# Experiment: ai-leetcode-lab, round 1
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        import random
        self.random=random;self.limit=n-len(blacklist);blocked=set(blacklist);self.mapping={};tail=iter(x for x in range(self.limit,n)if x not in blocked)
        for value in blacklist:
            if value<self.limit:self.mapping[value]=next(tail)

    def pick(self) -> int:
        value=self.random.randrange(self.limit);return self.mapping.get(value,value)


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
