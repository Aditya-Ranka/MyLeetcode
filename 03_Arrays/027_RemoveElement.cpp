/*
Problem: Remove Element
LeetCode: https://leetcode.com/problems/remove-element/description/
Topic: Array, Two Pointers
Difficulty: Easy  

Problem Description:
- Given an integer array nums and an integer val, remove all occurrences of val in-place.
- The relative order of the elements may be changed.
- Return k, the number of elements in nums which are not equal to val.
- It must be done with O(1) extra memory; you should modify nums in-place such that the first k elements
  of nums contain the elements that are not equal to val (the rest can be anything).

Approach:
- Use two pointers:
  - i: iterates through the array
  - k: tracks the position where the next kept element should be written
- For each nums[i], if nums[i] != val, assign nums[k] = nums[i] and increment k.
- At the end, k is the length of the array without val, and nums[0..k-1] holds the kept elements.

Time Complexity: O(n)
Space Complexity: O(1)
*/



class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int right = nums.size() - 1;
        int k = 0;
        int left = 0;
        for(left; left <= right;left++){
        if(nums[left] == val){
            k++;
            nums[left] = nums[right];
            left--;
            right--;
        }
        }
    return left;
    }
};
