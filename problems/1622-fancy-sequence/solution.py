# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:34Z
# Experiment: ai-leetcode-lab, round 1
class Fancy:

    def __init__(self):
        self.mod=1_000_000_007;self.values=[];self.total=0;self.base=0;self.prefix_value=0;self.multiplier=1;self.increment=0

    def append(self, val: int) -> None:
        normalized=(val-self.increment)*pow(self.multiplier,self.mod-2,self.mod)%self.mod;self.values.append(normalized);self.total+=1

    def addAll(self, inc: int) -> None:
        self.increment=(self.increment+inc)%self.mod;self.prefix_value=(self.prefix_value+inc)%self.mod

    def multAll(self, m: int) -> None:
        if m%self.mod==0:
            self.base=self.total;self.values=[];self.prefix_value=0;self.multiplier=1;self.increment=0
        else:
            self.multiplier=self.multiplier*m%self.mod;self.increment=self.increment*m%self.mod;self.prefix_value=self.prefix_value*m%self.mod

    def getIndex(self, idx: int) -> int:
        if idx>=self.total:return -1
        if idx<self.base:return self.prefix_value
        return (self.values[idx-self.base]*self.multiplier+self.increment)%self.mod


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
