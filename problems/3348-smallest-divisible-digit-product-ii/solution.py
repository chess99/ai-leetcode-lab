# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Experiment: ai-leetcode-lab, escalation from round 1
class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        input_t = t
        factors = (
            (0, 0, 0, 0),  # 0 is never used
            (0, 0, 0, 0),
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (2, 0, 0, 0),
            (0, 0, 1, 0),
            (1, 1, 0, 0),
            (0, 0, 0, 1),
            (3, 0, 0, 0),
            (0, 2, 0, 0),
        )

        required = []
        for prime in (2, 3, 5, 7):
            exponent = 0
            while t % prime == 0:
                t //= prime
                exponent += 1
            required.append(exponent)
        if t != 1:
            return "-1"

        # Keep the original inputs as requested by the problem statement.
        vornitexis = (num, input_t)

        max_two, max_three = required[0], required[1]
        infinity = 10**9
        min_digits = [
            [infinity] * (max_three + 1) for _ in range(max_two + 1)
        ]
        min_digits[0][0] = 0
        for twos in range(max_two + 1):
            for threes in range(max_three + 1):
                if twos == 0 and threes == 0:
                    continue
                best = infinity
                for digit in range(2, 10):
                    take_two, take_three = factors[digit][:2]
                    next_two = max(0, twos - take_two)
                    next_three = max(0, threes - take_three)
                    if next_two == twos and next_three == threes:
                        continue
                    best = min(best, 1 + min_digits[next_two][next_three])
                min_digits[twos][threes] = best

        def shortest_length(state):
            twos, threes, fives, sevens = state
            return min_digits[twos][threes] + fives + sevens

        def smallest_tail(state):
            state = tuple(state)
            answer = []
            while shortest_length(state):
                current_length = shortest_length(state)
                for digit in range(2, 10):
                    contribution = factors[digit]
                    next_state = tuple(
                        max(0, state[index] - contribution[index])
                        for index in range(4)
                    )
                    if next_state != state and (
                        1 + shortest_length(next_state) == current_length
                    ):
                        answer.append(str(digit))
                        state = next_state
                        break
            return "".join(answer)

        n = len(num)
        # Four compact prefix arrays avoid storing O(n) Python tuples/lists.
        covered = [bytearray(n + 1) for _ in range(4)]
        first_zero = n
        for index, character in enumerate(num):
            digit = ord(character) - ord("0")
            if digit == 0 and first_zero == n:
                first_zero = index
            contribution = factors[digit]
            for prime_index in range(4):
                covered[prime_index][index + 1] = min(
                    required[prime_index],
                    covered[prime_index][index] + contribution[prime_index],
                )

        if first_zero == n and all(
            covered[index][n] >= required[index] for index in range(4)
        ):
            return num

        # A pivot to the right of the first zero would retain that zero.
        for index in range(min(first_zero, n - 1), -1, -1):
            old_digit = ord(num[index]) - ord("0")
            suffix_capacity = n - index - 1
            for digit in range(old_digit + 1, 10):
                contribution = factors[digit]
                remaining = tuple(
                    max(
                        0,
                        required[prime_index]
                        - covered[prime_index][index]
                        - contribution[prime_index],
                    )
                    for prime_index in range(4)
                )
                needed = shortest_length(remaining)
                if needed <= suffix_capacity:
                    tail = smallest_tail(remaining)
                    return (
                        num[:index]
                        + str(digit)
                        + "1" * (suffix_capacity - needed)
                        + tail
                    )

        tail = smallest_tail(tuple(required))
        answer_length = max(n + 1, len(tail))
        return "1" * (answer_length - len(tail)) + tail
