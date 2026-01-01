/*
Problem: Find Minimum in Rotated Sorted Array
LeetCode: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
Problem: Search A 2D Matrix
LeetCode: https://leetcode.com/problems/search-a-2d-matrix/description/
Topic: Binary Search
Difficulty: Medium  

Approach:
- Use binary search to find the pivot point (the minimum element).
- Compare mid element with the rightmost element to determine which half contains the minimum.
- If nums[mid] > nums[right], the minimum is in the right half.
- Otherwise, the minimum is in the left half (including mid).

Time Complexity: O(log n)
Space Complexity: O(1)
- Basic hint was that mentioned time complexity was O(log(m*n)) so we can think of binary search.
- So double binary Search:
    1. rows 
    2. columns


Time Complexity: O(log(m*n))
Space Complexity: O(1) if we don't consider the space for the output array. 
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

