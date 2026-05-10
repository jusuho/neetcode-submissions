# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return
        
        queue = deque()
        # 1. 先把 head 後面的所有節點放進 queue (head 本身可以不用放，從它開始接)
        curr = head.next
        while curr:
            queue.append(curr)
            curr = curr.next
        
        # 2. 開始交替串接
        curr = head
        for i in range(len(queue)):
            # 偶數次取右邊 (pop)，奇數次取左邊 (popleft)？ 
            # 不對，根據題目 [0, n, 1, n-1...]，第一步要接最後一個
            if i % 2 == 0:
                curr.next = queue.pop()
            else:
                curr.next = queue.popleft()
            
            curr = curr.next
            
        # 3. 最關鍵的一步：把最後一個節點的 next 指向 None，避免產生環
        curr.next = None