class ListNode:
    def __init__(self, key, val=-1):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.map = [ListNode(0) for i in range(10**4)]

    def put(self, key: int, value: int) -> None:
        cur = self.map[key % len(self.map)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.map[key % len(self.map)]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.map[key % len(self.map)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next