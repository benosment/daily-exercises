class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        odd = head
        even = head.next
        first_even = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = first_even
        return head

def addLL(head, val):
    node = ListNode(val)
    node.next = head
    return node

if __name__ == '__main__':
    s = Solution()
    head = addLL(None, 4)
    head = addLL(head, 3)
    head = addLL(head, 2)
    head = addLL(head, 1)
    ans = s.oddEvenList(head)
