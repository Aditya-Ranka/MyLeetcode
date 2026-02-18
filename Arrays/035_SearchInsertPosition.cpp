/*
Problem: Search Insert Position
LeetCode: https://leetcode.com/problems/search-insert-position/description/
Topic: Array, Binary Search
Difficulty: Easy

Problem Description:
- Given a sorted array of integers, find the index where a target value should be inserted to maintain sorted order.
- The array is non-empty and sorted in ascending order.
- If the target is already in the array, the function should return its index.
- If the target is not in the array, the function should return the index where it should be inserted.

Approach:
- The code uses a binary search algorithm to find the target in the array, utilizing the variables 'left' and 'right' to track the search range.
- The 'mid' variable is used to calculate the middle index of the current search range.
- If the target is not found, the function returns the 'left' index, which represents the position where the target should be inserted to maintain sorted order.
- The binary search approach allows for efficient searching of the array with a minimal number of comparisons.

Time Complexity: O(log n)
Space Complexity: O(1)
*/

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        while (left <= right) {   
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            else if (nums[mid] < target) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
        return left;
    }
};
