# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        if count - n == 0:
            return head.next
        else:

            temp = head
            for i in range(count - 1):
                if i + 1 == count - n:
                    temp.next = temp.next.next
                    break
                temp = temp.next
        return head



            