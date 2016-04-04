# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        iter = head
        while iter and ter.next:
            if iter.next.val == iter.val:
                iter.next = iter.next.next
            else:
                iter = iter.next
        return head

def remove_dupes(head):
    iter = head
    seen = {}
    seen[head.val] = 1
    while iter:
        if iter.next:
           if iter.next.val in seen:
               iter.next = iter.next.next
           else:
               seen[iter.val] = 1
        iter = iter.next
    return head


def remove_dupes(head):
    iter = head
    while iter.next:
        if iter.next.val == iter.val:
           iter.next = iter.next.next
        else:
           iter = iter.next
    return head


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addLL(head, val):
    node = ListNode(val)
    node.next = head
    return node

if __name__ == '__main__':
    s = Solution()
    head = addLL(None, 4)
    head = addLL(head, 3)
    head = addLL(head, 2)
    head = addLL(head, 2)
    head = addLL(head, 2)
    head = addLL(head, 1)
    ans = s.deleteDuplicates(head)
