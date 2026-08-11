# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:19:08Z
# Experiment: ai-leetcode-lab, round 1
class OrderedStream:

    def __init__(self, n: int):
        self.values=['']*(n+1); self.pointer=1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.values[idKey]=value; result=[]
        while self.pointer<len(self.values) and self.values[self.pointer]: result.append(self.values[self.pointer]); self.pointer+=1
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
