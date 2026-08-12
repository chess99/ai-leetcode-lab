# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:47Z
# Experiment: ai-leetcode-lab, round 1
class RangeModule:

    def __init__(self):
        self.intervals=[]

    def addRange(self, left: int, right: int) -> None:
        result=[];start,end=left,right
        for a,b in self.intervals:
            if b<start:result.append([a,b])
            elif end<a:result.append([start,end]);start,end=a,b
            else:start=min(start,a);end=max(end,b)
        result.append([start,end]);self.intervals=result

    def queryRange(self, left: int, right: int) -> bool:
        return any(a<=left and right<=b for a,b in self.intervals)

    def removeRange(self, left: int, right: int) -> None:
        result=[]
        for a,b in self.intervals:
            if b<=left or a>=right:result.append([a,b])
            else:
                if a<left:result.append([a,left])
                if b>right:result.append([right,b])
        self.intervals=result


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
