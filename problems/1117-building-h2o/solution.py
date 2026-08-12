# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:21:14Z
# Experiment: ai-leetcode-lab, round 1
from threading import Barrier, Semaphore


class H2O:
    def __init__(self):
        self.hydrogen_slots = Semaphore(2)
        self.oxygen_slots = Semaphore(1)
        self.molecule_ready = Barrier(3)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.hydrogen_slots.acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.molecule_ready.wait()
        self.hydrogen_slots.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.oxygen_slots.acquire()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.molecule_ready.wait()
        self.oxygen_slots.release()
