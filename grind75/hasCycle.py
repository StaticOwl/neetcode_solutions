#Logic: Keeping track of heads in a data structure (dict here) and calling a recursion given scenario if head is in track then return True, else: defaults to false

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode], visited={}) -> bool:
        if head:
            if head in visited:
                return True
            else:
                visited[head]=True
                return self.hasCycle(head.next, visited)
        else:
            return False

# No Space Approach

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        return False

# Both goes about time complexity O(n)