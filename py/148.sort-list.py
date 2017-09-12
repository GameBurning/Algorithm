# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        p = head
        q = p.next
        length = 1
        while q is not None and q.next is not None:
            p = p.next
            q = q.next.next
            length += 1
        if q is None:
            return self.merge(head, length - 1, p, length)
        else:
            return self.merge(head, length, p.next, length)

    def merge(self, head1, length1, head2, length2):
        dummy = ListNode(0)
        if length1 >= 2:
            p = head1
            for step in range(length1 // 2):
                p = p.next
            head1 = self.merge(head1, length1 // 2, p, length1 - length1 // 2)
        if length2 >= 2:
            p = head2
            for step in range(length2 // 2):
                p = p.next
            head2 = self.merge(head2, length2 // 2, p, length2 - length2 // 2)
        p = dummy

        while True:
            if length1 == 0:
                p.next = head2
                return dummy.next
            if length2 == 0:
                for i in range(length1):
                    p.next = head1
                    p = p.next
                    head1 = head1.next
                p.next = None
                return dummy.next
            if head1.val <= head2.val:
                p.next = head1
                p = p.next
                head1 = head1.next
                length1 -= 1
            else:
                p.next = head2
                p = p.next
                head2 = head2.next
                length2 -= 1
