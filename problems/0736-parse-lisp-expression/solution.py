# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:48Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def evaluate(self, expression: str) -> int:
        index = 0

        def token():
            nonlocal index
            start = index
            while index < len(expression) and expression[index] not in ' ()':
                index += 1
            return expression[start:index]

        def value(name, environment):
            return int(name) if name[0] == '-' or name[0].isdigit() else environment[name]

        def parse(environment):
            nonlocal index
            if expression[index] != '(':
                return value(token(), environment)
            index += 1
            operation = token()
            index += 1
            if operation in ('add', 'mult'):
                first = parse(environment)
                index += 1
                second = parse(environment)
                index += 1
                return first + second if operation == 'add' else first * second

            local = environment.copy()
            while True:
                if expression[index] == '(':
                    result = parse(local)
                    index += 1
                    return result
                name = token()
                if expression[index] == ')':
                    index += 1
                    return value(name, local)
                index += 1
                local[name] = parse(local)
                index += 1

        return parse({})
