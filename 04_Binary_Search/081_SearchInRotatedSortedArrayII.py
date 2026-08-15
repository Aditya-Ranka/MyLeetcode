"""
Problem: Search in Rotated Sorted Array II
LeetCode: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
Topic: Binary Search
Difficulty: Medium

Approach:
- Rotated binary search that tolerates duplicates.
- When nums[l]==nums[mid] or nums[r]==nums[mid] you can't tell which half is sorted, so shrink that end by one (this is what makes the worst case O(n)).
- Otherwise find the sorted half (nums[l] < nums[mid] => left sorted) and check whether target lies inside it to pick a side.

Time Complexity: O(log n) average, O(n) worst
Space Complexity: O(1)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid]:
                l+=1
                continue
            if nums[r] == nums[mid]:
                r-=1
                continue
            if nums[l] < nums[mid]: #left half is sorted
                if  nums[l] <= target < nums[mid]: 
                    r = mid - 1
                    continue
                else:
                    l = mid + 1
                    continue
            if nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                    continue
                else:
                    r = mid - 1
                    continue
        return False
