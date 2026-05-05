# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        lst = []
        curr = head
        while curr:
            lst.append(curr)
            curr = curr.next

        a = len(lst) - n
        if a == 0:
            return head.next
        elif a == len(lst) - 1:
            lst[a - 1].next = None
        else:
            lst[a - 1].next = lst[a - 1].next.next
        return head