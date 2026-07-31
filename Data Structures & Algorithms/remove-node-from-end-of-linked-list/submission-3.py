# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while head:
            count+=1
            head = head.next
        length = count - n
        if length ==0 :
            return temp.next
        
        else:
            head = temp
            while length-1 :
                head = head.next
                length-=1
            
            head.next = head.next.next
            head = temp
            return head

                
        
        