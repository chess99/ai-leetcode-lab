# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:01Z
# Experiment: ai-leetcode-lab, round 1
class FreqStack:

    def __init__(self):
        from collections import defaultdict
        self.count=defaultdict(int);self.groups=defaultdict(list);self.maximum=0

    def push(self, val: int) -> None:
        self.count[val]+=1;self.maximum=max(self.maximum,self.count[val]);self.groups[self.count[val]].append(val)

    def pop(self) -> int:
        value=self.groups[self.maximum].pop();self.count[value]-=1
        if not self.groups[self.maximum]:self.maximum-=1
        return value


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
