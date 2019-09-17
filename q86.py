# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import * 

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if(head == None):
            return head
        pqueue = []
        current = head
        index = 0
        while(current != None):
            if(current.val < x):
                heappush(pqueue, (1, index, current.val))
            else: 
                heappush(pqueue, (2, index, current.val))
            current = current.next
            index += 1
        newhead = ListNode(heappop(pqueue)[2])
        current = newhead
        while(len(pqueue) > 0):
            current.next = ListNode(heappop(pqueue)[2])
            current = current.next
        return newhead