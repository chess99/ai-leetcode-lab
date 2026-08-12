# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:23Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king=kingName;self.children=defaultdict(list);self.dead=set()

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order=[]
        stack=[self.king]
        while stack:
            name=stack.pop()
            if name not in self.dead:order.append(name)
            stack.extend(reversed(self.children[name]))
        return order


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
