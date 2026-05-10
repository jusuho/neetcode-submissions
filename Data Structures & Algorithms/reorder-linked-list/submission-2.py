# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev 
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        # notice that reversed 2nd half list
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # slow == 1/2 flow
        second = slow.next
        slow.next = None
        second = self.reverse(second)

        l1 = head
        l2 = second
        while l1 and l2:
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2
            l2.next = l1_next

            l1 = l1_next
            l2 = l2_next

