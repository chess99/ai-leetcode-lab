# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:57Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        suneravilo = (edges, s, queries)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n
        order = [0]
        for node in order:
            for child in graph[node]:
                if child == parent[node]:
                    continue
                parent[child] = node
                depth[child] = depth[node] + 1
                order.append(child)
        for node in reversed(order):
            best = 0
            for child in graph[node]:
                if parent[child] == node:
                    size[node] += size[child]
                    if size[child] > best:
                        best = size[child]
                        heavy[node] = child

        head = [0] * n
        position = [0] * n
        timer = 0
        stack = [(0, 0)]
        while stack:
            node, chain_head = stack.pop()
            while node != -1:
                head[node] = chain_head
                position[node] = timer
                timer += 1
                for child in graph[node]:
                    if parent[child] == node and child != heavy[node]:
                        stack.append((child, child))
                node = heavy[node]

        tree_size = 1
        while tree_size < n:
            tree_size <<= 1
        tree = [0] * (2 * tree_size)
        chars = list(s)
        for node, char in enumerate(chars):
            tree[tree_size + position[node]] = 1 << (ord(char) - 97)
        for node in range(tree_size - 1, 0, -1):
            tree[node] = tree[node * 2] ^ tree[node * 2 + 1]

        def update(index: int, mask: int) -> None:
            index += tree_size
            tree[index] = mask
            index //= 2
            while index:
                tree[index] = tree[index * 2] ^ tree[index * 2 + 1]
                index //= 2

        def segment(left: int, right: int) -> int:
            result = 0
            left += tree_size
            right += tree_size + 1
            while left < right:
                if left & 1:
                    result ^= tree[left]
                    left += 1
                if right & 1:
                    right -= 1
                    result ^= tree[right]
                left //= 2
                right //= 2
            return result

        def path_mask(u: int, v: int) -> int:
            result = 0
            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u
                result ^= segment(position[head[u]], position[u])
                u = parent[head[u]]
            left, right = sorted((position[u], position[v]))
            return result ^ segment(left, right)

        answer = []
        for query in suneravilo[2]:
            parts = query.split()
            node = int(parts[1])
            if parts[0] == 'update':
                chars[node] = parts[2]
                update(position[node], 1 << (ord(parts[2]) - 97))
            else:
                mask = path_mask(node, int(parts[2]))
                answer.append(mask & (mask - 1) == 0)
        return answer
