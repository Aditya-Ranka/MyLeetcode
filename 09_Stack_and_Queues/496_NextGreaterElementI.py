"""
Problem: Next Greater Element I
LeetCode: https://leetcode.com/problems/next-greater-element-i/
Topic: Stack and Queues
Difficulty: Easy

Approach:
- Map each nums1 value to its index
- Initialize result list with -1 and an empty stack
- Iterate over nums2, popping smaller stack elements and recording their next greater
- Assign the current nums2 element as the next greater for each popped value
- Push the current element onto the stack only if it appears in nums1

Comments:
- Assumes all numbers are distinct and that nums1 is a subset of nums2, as guaranteed by the problem

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = {n:i for i,n in enumerate(nums1)}
        res = [-1] * len(nums1)
        stck = []
        for i in range(len(nums2)):
            while stck and stck[-1] < nums2[i]:
                res[hashMap[stck[-1]]] = nums2[i]
                stck.pop()
            if nums2[i] in hashMap:
                stck.append(nums2[i])
            
        return res
