# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = []
        if not head:
            return head
        while head:
            temp = ListNode()
            temp.val = head.val
            head = head.next
            if prev:
                temp.next = prev[-1]
            prev.append(temp)

        return temp