"""
Problem: Merge Two Sorted Lists
LeetCode: https://leetcode.com/problems/merge-two-sorted-lists/
Topic: Linked List
Difficulty: Easy

Approach:
- Check if either input list is None and return the other
- Create a dummy ListNode and keep a pointer to its head
- Iterate while both lists have nodes, link the smaller node to the result and advance pointers
- Append any remaining nodes from the non‑exhausted list
- Return the merged list starting after the dummy node

Comments:
- Uses a dummy node to simplify linking; modifies the original nodes in‑place, so no extra list nodes are allocated

Time Complexity: O(n+m)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        res = ListNode()
        ret = res
        while list1 and list2:
            if list1.val > list2.val:
                res.next = list2
                list2 = list2.next
            else:
                res.next = list1
                list1 = list1.next
            res = res.next
            
        while list1:
            res.next = list1
            list1 = list1.next
            res = res.next
        while list2:
            res.next = list2
            list2 = list2.next
            res = res.next
        return ret.next
