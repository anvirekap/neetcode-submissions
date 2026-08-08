# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1. Create a dummy node to anchor the result
        dummy = ListNode()
        tail = dummy
        
        # 2. Compare elements from both lists
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        # 3. Attach remaining nodes from whichever list is not empty
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        return dummy.next