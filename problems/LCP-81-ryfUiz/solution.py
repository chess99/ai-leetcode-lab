# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:24Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def getNandResult(self, k: int, arr: List[int], operations: List[List[int]]) -> int:
        mask = (1 << k) - 1
        n = len(arr); size = 1
        while size < n: size <<= 1
        # A transform is (value for input bit 0, value for input bit 1).
        tree = [(0, mask)] * (2 * size)
        def leaf(a): return (mask, mask ^ a)
        def join(f, g): # g(f(x))
            return (g[0] ^ (f[0] & (g[0] ^ g[1])),
                    g[0] ^ (f[1] & (g[0] ^ g[1])))
        for i, a in enumerate(arr): tree[size+i] = leaf(a)
        for i in range(size-1, 0, -1): tree[i] = join(tree[i*2], tree[i*2+1])
        def power(f, exp):
            result = (0, mask)
            while exp:
                if exp & 1: result = join(result, f)
                f = join(f, f); exp >>= 1
            return result
        ans = 0
        for typ, x, y in operations:
            if typ == 0:
                arr[x] = y; p = size + x; tree[p] = leaf(y); p //= 2
                while p:
                    tree[p] = join(tree[p*2], tree[p*2+1]); p //= 2
            else:
                f = power(tree[1], x)
                ans ^= f[0] ^ (y & (f[0] ^ f[1]))
        return ans
