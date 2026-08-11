# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:04:52Z
# Experiment: ai-leetcode-lab, round 1
class MyHashMap:

    def __init__(self):
        self.values={}

    def put(self, key: int, value: int) -> None:
        self.values[key]=value

    def get(self, key: int) -> int:
        return self.values.get(key,-1)

    def remove(self, key: int) -> None:
        self.values.pop(key,None)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
