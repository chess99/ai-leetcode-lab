# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:53:39Z
# Experiment: ai-leetcode-lab, round 1
class ExamRoom:

    def __init__(self, n: int):
        self.n=n; self.seats=[]

    def seat(self) -> int:
        if not self.seats: self.seats.append(0); return 0
        best_distance,best= self.seats[0],0
        for left,right in zip(self.seats,self.seats[1:]):
            distance=(right-left)//2
            if distance>best_distance: best_distance,best=distance,left+distance
        if self.n-1-self.seats[-1]>best_distance: best=self.n-1
        import bisect; bisect.insort(self.seats,best); return best

    def leave(self, p: int) -> None:
        self.seats.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
