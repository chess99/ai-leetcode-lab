# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:01:00Z
# Experiment: ai-leetcode-lab, round 1
class Operations:

    def __init__(self):
        pass

    def minus(self, a: int, b: int) -> int:
        return a + self._negate(b)

    def multiply(self, a: int, b: int) -> int:
        if a == 0 or b == 0:
            return 0
        negative = (a < 0) != (b < 0)
        a = self._abs(a)
        b = self._abs(b)
        if a < b:
            a, b = b, a
        chunks = []
        factor = 1
        while factor <= b:
            chunks.append((factor, a))
            factor += factor
            a += a
        result = 0
        for factor, addend in reversed(chunks):
            if factor <= b:
                b += self._negate(factor)
                result += addend
        return self._negate(result) if negative else result

    def divide(self, a: int, b: int) -> int:
        negative = (a < 0) != (b < 0)
        dividend = self._abs(a)
        divisor = self._abs(b)
        chunks = []
        multiple = 1
        current = divisor
        while current <= dividend:
            chunks.append((current, multiple))
            current += current
            multiple += multiple
        quotient = 0
        for current, multiple in reversed(chunks):
            if current <= dividend:
                dividend += self._negate(current)
                quotient += multiple
        return self._negate(quotient) if negative else quotient

    def _negate(self, value: int) -> int:
        if value == 0:
            return 0
        delta = -1 if value > 0 else 1
        chunks = []
        step = delta
        if value > 0:
            while value + step >= 0:
                chunks.append(step)
                step += step
        else:
            while value + step <= 0:
                chunks.append(step)
                step += step
        result = 0
        for step in reversed(chunks):
            if (value > 0 and value + step >= 0) or (value < 0 and value + step <= 0):
                value += step
                result += step
        return result

    def _abs(self, value: int) -> int:
        return self._negate(value) if value < 0 else value


# Your Operations object will be instantiated and called as such:
# obj = Operations()
# param_1 = obj.minus(a,b)
# param_2 = obj.multiply(a,b)
# param_3 = obj.divide(a,b)
