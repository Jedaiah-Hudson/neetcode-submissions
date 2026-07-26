# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        seen = []
        curr = head
        while curr.next:
            if curr.val in seen:
                return True
            seen.append(curr.val)
            curr = curr.next 
        return False
