#!/usr/bin/env python3

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        s = str(self.val)
        if self.next:
            s += '->' + str(self.next)
        return s

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        new_head = head.next
        old_head = head
        tmp = new_head.next
        head = new_head
        head.next = old_head
        old_head.next = self.swapPairs(tmp)
        return head

def addLL(head, val):
    node = ListNode(val)
    node.next = head
    return node

if __name__ == '__main__':
    s = Solution()
    ll = addLL(None, 4)
    ll = addLL(ll, 3)
    ll = addLL(ll, 2)
    ll = addLL(ll, 1)
    ll = addLL(ll, 0)
    l = None
    print(ll)
    print(s.swapPairs(ll))
