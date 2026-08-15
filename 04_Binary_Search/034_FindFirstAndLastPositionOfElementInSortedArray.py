"""
Problem: Find First and Last Position of Element in Sorted Array
LeetCode: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Topic: Binary Search
Difficulty: Medium

Approach:
- Two binary searches over the sorted array.
- findFirst: on a match, record mid and keep searching LEFT (r = mid-1).
- findEnd: on a match, record mid and keep searching RIGHT (l = mid+1).
- Return [first, last]; both -1 when the target is absent.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst():
            l, r = 0, len(nums) - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    ans = mid        
                    r = mid - 1     
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return ans

        def findEnd():
            l, r = 0, len(nums) - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    ans = mid        
                    l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return ans

        return [findFirst(), findEnd()]
