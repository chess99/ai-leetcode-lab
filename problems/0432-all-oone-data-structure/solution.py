# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:15Z
# Experiment: ai-leetcode-lab, round 1
class Bucket:
    def __init__(self, count=0):
        self.count = count
        self.keys = set()
        self.previous = self.next = None


class AllOne:

    def __init__(self):
        self.head, self.tail = Bucket(), Bucket()
        self.head.next, self.tail.previous = self.tail, self.head
        self.locations = {}

    def _insert_after(self, node, bucket):
        bucket.previous, bucket.next = node, node.next
        node.next.previous = bucket
        node.next = bucket

    def _remove(self, bucket):
        bucket.previous.next = bucket.next
        bucket.next.previous = bucket.previous

    def inc(self, key: str) -> None:
        if key not in self.locations:
            bucket = self.head.next
            if bucket is self.tail or bucket.count != 1:
                bucket = Bucket(1)
                self._insert_after(self.head, bucket)
            bucket.keys.add(key)
            self.locations[key] = bucket
            return
        current = self.locations[key]
        following = current.next
        if following is self.tail or following.count != current.count + 1:
            following = Bucket(current.count + 1)
            self._insert_after(current, following)
        following.keys.add(key)
        self.locations[key] = following
        current.keys.remove(key)
        if not current.keys:
            self._remove(current)

    def dec(self, key: str) -> None:
        current = self.locations[key]
        current.keys.remove(key)
        if current.count == 1:
            del self.locations[key]
        else:
            previous = current.previous
            if previous is self.head or previous.count != current.count - 1:
                previous = Bucket(current.count - 1)
                self._insert_after(current.previous, previous)
            previous.keys.add(key)
            self.locations[key] = previous
        if not current.keys:
            self._remove(current)

    def getMaxKey(self) -> str:
        return '' if self.tail.previous is self.head else next(iter(self.tail.previous.keys))

    def getMinKey(self) -> str:
        return '' if self.head.next is self.tail else next(iter(self.head.next.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
