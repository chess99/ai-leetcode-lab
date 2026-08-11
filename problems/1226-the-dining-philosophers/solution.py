# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:28:42Z
# Experiment: ai-leetcode-lab, round 1
from threading import Lock, Semaphore
class DiningPhilosophers:
    def __init__(self):
        self.forks=[Lock() for _ in range(5)]
        self.room=Semaphore(4)
    def wantsToEat(self, philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork):
        left,right=philosopher,(philosopher+1)%5
        self.room.acquire(); self.forks[left].acquire(); pickLeftFork(); self.forks[right].acquire(); pickRightFork()
        eat(); putRightFork(); self.forks[right].release(); putLeftFork(); self.forks[left].release(); self.room.release()
