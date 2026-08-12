# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:22Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
        n=len(vals);g=[[]for _ in range(n)]
        for i in range(1,n):g[par[i]].append(i)
        xor=[0]*n;tin=[0]*n;tout=[0]*n;order=[];st=[(0,0,vals[0])]
        while st:
            u,state,x=st.pop()
            if not state:
                tin[u]=len(order);order.append(u);xor[u]=x;st.append((u,1,x))
                for v in reversed(g[u]):st.append((v,0,x^vals[v]))
            else:tout[u]=len(order)
        # All subtree node sets are Euler intervals.  Mo's ordering lets us
        # maintain value frequencies; a Fenwick tree contains one at every
        # XOR value currently occurring at least once.
        width = max(xor).bit_length() or 1
        size = 1 << width
        bit = [0] * (size + 1)
        freq = [0] * size
        def add_bit(index, delta):
            index += 1
            while index <= size:
                bit[index] += delta; index += index & -index
        def kth(k):
            if bit[size] < k: return -1
            index = 0; step = 1 << (size.bit_length() - 1)
            while step:
                nxt = index + step
                if nxt <= size and bit[nxt] < k:
                    index = nxt; k -= bit[nxt]
                step >>= 1
            return index
        block = max(1, int(n ** 0.5))
        packed = [(tin[u], tout[u] - 1, k, qi) for qi, (u, k) in enumerate(queries)]
        packed.sort(key=lambda q: (q[0] // block, q[1] if (q[0] // block) % 2 == 0 else -q[1]))
        answer = [-1] * len(queries); left = 0; right = -1
        def include(pos):
            value = xor[order[pos]]; freq[value] += 1
            if freq[value] == 1: add_bit(value, 1)
        def exclude(pos):
            value = xor[order[pos]]; freq[value] -= 1
            if not freq[value]: add_bit(value, -1)
        for l, r, k, qi in packed:
            while left > l: left -= 1; include(left)
            while right < r: right += 1; include(right)
            while left < l: exclude(left); left += 1
            while right > r: exclude(right); right -= 1
            answer[qi] = kth(k)
        return answer
