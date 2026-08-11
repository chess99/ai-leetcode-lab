# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:28:39Z
# Experiment: ai-leetcode-lab, round 1
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        from threading import Condition
        self.current = 1
        self.condition = Condition()

    def _run(self, predicate, callback) -> None:
        while True:
            with self.condition:
                while self.current <= self.n and not predicate(self.current):
                    self.condition.wait()
                if self.current > self.n:
                    self.condition.notify_all()
                    return
                callback()
                self.current += 1
                self.condition.notify_all()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        self._run(lambda value: value % 3 == 0 and value % 5 != 0, printFizz)

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        self._run(lambda value: value % 5 == 0 and value % 3 != 0, printBuzz)

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        self._run(lambda value: value % 15 == 0, printFizzBuzz)

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        self._run(lambda value: value % 3 != 0 and value % 5 != 0, lambda: printNumber(self.current))
