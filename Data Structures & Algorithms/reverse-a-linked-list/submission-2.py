# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        # nxt = curr.next
        # None(prev) 1(curr)-> 2(nxt)->3->None
        while curr:
            nxt = curr.next #None 1(curr)->2(nxt) #phase2: None <-1(prev), 2(curr)->3(nxt) #None<-1<-2, 3->None(nxt)
            curr.next = prev # None(prev)<-1(curr) # phase2: None<-1(prev)<-2(curr), 3(nxt) #None<-1<-2<-3 None
            prev = curr # None <-1(curr, prev), 2(nxt) #phase2: None<-1<-2(curr, prev), 3(nxt) #None<-1<-2<-3(prev) 
            curr = nxt # None <-1(prev), 2(curr, nxt) #phase2: None<-1<-2(prev), 3(nxt, curr) 
        

        return prev
