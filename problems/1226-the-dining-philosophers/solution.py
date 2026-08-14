# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Created: 2026-08-14
# Experiment: ai-leetcode-lab, round 1
from threading import Condition


class DiningPhilosophers:
    def __init__(self):
        self.condition = Condition()
        self.next_ticket = 0
        self.serving = 0

    def wantsToEat(
        self,
        philosopher,
        pickLeftFork,
        pickRightFork,
        eat,
        putLeftFork,
        putRightFork,
    ):
        with self.condition:
            ticket = self.next_ticket
            self.next_ticket += 1
            while ticket != self.serving:
                self.condition.wait()

        try:
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()
        finally:
            with self.condition:
                self.serving += 1
                self.condition.notify_all()
