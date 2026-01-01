/*
Problem: Find Minimum in Rotated Sorted Array
LeetCode: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
Topic: Binary Search
Difficulty: Medium  

Approach:
- Use binary search to find the pivot point (the minimum element).
- Compare mid element with the rightmost element to determine which half contains the minimum.
- If nums[mid] > nums[right], the minimum is in the right half.
- Otherwise, the minimum is in the left half (including mid).

Time Complexity: O(log n)
Space Complexity: O(1)
*/


class Solution {
    public:
        int findMin(vector<int>& nums) {
            int l = 0;
            int r = nums.size() -1;
            while (l < r){
                int m = l + (r-l)/2;
                if(nums[m] > nums[r]){
                    l = m+1;
                }
                else{
                    r = m;
                }
            }
            return nums[l];
        }
    };

