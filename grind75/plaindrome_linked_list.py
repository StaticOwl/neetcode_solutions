# Solution with time O(n). I am doing the full reversal of the linkedlist
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        if not head:
            return True
        root = head
        while head:
            temp = ListNode()
            temp.val = head.val
            head = head.next
            temp.next = prev
            prev = temp

        while root:
            if root.val != temp.val:
                return False
            else:
                root = root.next
                temp = temp.next
        return True

#with constant space and mid reversal
#This also have a nice algorigthm for reversing the list
#TODO: Update reverse LinkedList code with constant space
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next or not head:
            return True
        
        mid = head
        end = head
        prev = None
        while end and end.next:
            end = end.next.next
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        if end:
            mid = mid.next
        
        while prev and mid:
            if prev.val != mid.val:
                return False
            prev = prev.next
            mid = mid.next
        return True