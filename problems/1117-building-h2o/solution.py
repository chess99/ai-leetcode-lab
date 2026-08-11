# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:21:14Z
# Experiment: ai-leetcode-lab, round 1
from threading import Semaphore


class H2O:
    def __init__(self):
        self.hydrogen_slots = Semaphore(2)
        self.oxygen_ready = Semaphore(0)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.hydrogen_slots.acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.oxygen_ready.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.oxygen_ready.acquire()
        self.oxygen_ready.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.hydrogen_slots.release()
        self.hydrogen_slots.release()
