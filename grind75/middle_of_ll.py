# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        count = 0
        while head:
            count += 1
            head = head.next
        
        count = count // 2
        while count!=0:
            temp = temp.next
            count -=1
        return temp

#Single Loop Solution: Logic is fast will run twice as slow. so we don't need to use count to check and we can run this in one loop only.
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow