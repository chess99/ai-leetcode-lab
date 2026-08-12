# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:50Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        values = dict(zip(evalvars, evalints))
        tokens = expression.replace('(', '( ').replace(')', ' )').split()
        index = 0

        def add(first, second, sign=1):
            result = first.copy()
            for term, coefficient in second.items():
                result[term] += sign * coefficient
                if result[term] == 0:
                    del result[term]
            return result

        def multiply(first, second):
            result = Counter()
            for term1, coefficient1 in first.items():
                for term2, coefficient2 in second.items():
                    result[tuple(sorted(term1 + term2))] += coefficient1 * coefficient2
            for term in list(result):
                if result[term] == 0:
                    del result[term]
            return result

        def factor():
            nonlocal index
            current = tokens[index]
            index += 1
            if current == '(':
                result = expression_value()
                index += 1
                return result
            if current.lstrip('-').isdigit():
                return Counter({(): int(current)})
            if current in values:
                return Counter({(): values[current]})
            return Counter({(current,): 1})

        def product():
            nonlocal index
            result = factor()
            while index < len(tokens) and tokens[index] == '*':
                index += 1
                result = multiply(result, factor())
            return result

        def expression_value():
            nonlocal index
            result = product()
            while index < len(tokens) and tokens[index] in ('+', '-'):
                operation = tokens[index]
                index += 1
                result = add(result, product(), 1 if operation == '+' else -1)
            return result

        polynomial = expression_value()
        ordered = sorted(
            ((term, coefficient) for term, coefficient in polynomial.items() if coefficient),
            key=lambda item: (-len(item[0]), item[0]),
        )
        return ['*'.join((str(coefficient),) + term) for term, coefficient in ordered]
