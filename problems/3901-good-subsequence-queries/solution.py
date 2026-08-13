# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-13T00:00:00Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def countGoodSubseq(self, nums: list[int], p: int, queries: list[list[int]]) -> int:
        norqaveliq = (nums, p, queries)
        n = len(nums)
        limit = max(nums + [query[1] for query in queries]) // p

        smallest_prime = list(range(limit + 1))
        if limit >= 1:
            smallest_prime[1] = 1
        for i in range(2, int(limit**0.5) + 1):
            if smallest_prime[i] == i:
                for multiple in range(i * i, limit + 1, i):
                    if smallest_prime[multiple] == multiple:
                        smallest_prime[multiple] = i

        def prime_factors(value: int) -> list[int]:
            result = []
            while value > 1:
                prime = smallest_prime[value]
                result.append(prime)
                while value % prime == 0:
                    value //= prime
            return result

        prime_count: dict[int, int] = {}
        prime_xor: dict[int, int] = {}
        count_frequency: dict[int, int] = {}
        forbidden_by_index = [0] * n
        forbidden_indices = 0
        all_indices_xor = 0
        for i in range(n):
            all_indices_xor ^= i

        def alter_forbidden(prime: int, delta: int) -> None:
            nonlocal forbidden_indices
            missing = all_indices_xor ^ prime_xor[prime]
            if delta == 1:
                if forbidden_by_index[missing] == 0:
                    forbidden_indices += 1
                forbidden_by_index[missing] += 1
            else:
                forbidden_by_index[missing] -= 1
                if forbidden_by_index[missing] == 0:
                    forbidden_indices -= 1

        def alter_prime(prime: int, index: int, delta: int) -> None:
            old_count = prime_count.get(prime, 0)
            if old_count == n - 1:
                alter_forbidden(prime, -1)
            if old_count:
                count_frequency[old_count] -= 1

            new_count = old_count + delta
            prime_count[prime] = new_count
            prime_xor[prime] = prime_xor.get(prime, 0) ^ index
            if new_count:
                count_frequency[new_count] = count_frequency.get(new_count, 0) + 1
            if new_count == n - 1:
                alter_forbidden(prime, 1)

        eligible = 0
        factors_at_index: list[set[int]] = []
        for index, value in enumerate(nums):
            factors = set(prime_factors(value // p)) if value % p == 0 else set()
            factors_at_index.append(factors)
            if value % p == 0:
                eligible += 1
            for prime in factors:
                alter_prime(prime, index, 1)

        answer = 0
        for index, value in norqaveliq[2]:
            was_eligible = nums[index] % p == 0
            is_eligible = value % p == 0
            old_factors = factors_at_index[index]
            new_factors = set(prime_factors(value // p)) if is_eligible else set()

            if was_eligible:
                eligible -= 1
            if is_eligible:
                eligible += 1
            for prime in old_factors - new_factors:
                alter_prime(prime, index, -1)
            for prime in new_factors - old_factors:
                alter_prime(prime, index, 1)

            nums[index] = value
            factors_at_index[index] = new_factors

            whole_gcd_is_one = eligible > 0 and count_frequency.get(eligible, 0) == 0
            can_be_proper = eligible < n or forbidden_indices < n
            if whole_gcd_is_one and can_be_proper:
                answer += 1

        return answer
