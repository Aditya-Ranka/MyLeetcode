"""
Problem: Reverse Pairs
LeetCode: https://leetcode.com/problems/reverse-pairs/
Topic: Arrays
Difficulty: Hard

Approach:
- Count reverse pairs (i<j with nums[i] > 2*nums[j]) as a by-product of merge sort.
- After recursing on both halves, countPairs sweeps the two sorted halves with a moving pointer to count valid pairs.
- The standard merge then sorts the range so parent calls see sorted halves.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(low, mid, high):
            temp = []
            left = low
            right = mid+1
            while left <= mid and right <= high:
                if(nums[left] < nums[right]):
                    temp.append(nums[left])
                    left+=1
                else:
                    temp.append(nums[right])
                    right += 1
            while left <= mid:
                temp.append(nums[left])
                left+=1
            while right <= high:
                temp.append(nums[right])
                right+=1
            for i in range(low, high+1):
                nums[i] = temp[i-low]
        def mergesort(low, high):
            count=0
            if low>= high:
                return count
            m = (low + high)//2
            count+=mergesort(low, m)
            count+=mergesort(m+1, high)
            count+= countPairs(low, m, high)
            merge(low, m, high)
            return count
        def countPairs(low, mid, high):
            c = 0
            right = mid +1
            for i in range(low, mid+1):
                while right <= high and nums[right]*2 < nums[i]:
                    right+=1
                c+=right - mid - 1
            return c
        return mergesort(0,len(nums)-1)
