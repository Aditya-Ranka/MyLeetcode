/*
Problem: Search in Rotated Sorted Array
LeetCode: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
Topic: Binary Search
Difficulty: Medium  

Approach:
- Use binary search, but need to handle the rotated array.
- Determine which half (left or right) is sorted by comparing nums[mid] with nums[left].
- If left half is sorted and target is within [nums[left], nums[mid]), search left half.
- If right half is sorted and target is within (nums[mid], nums[right]], search right half.
- Otherwise, search the other half.

Time Complexity: O(log n)
Space Complexity: O(1)
*/


class Solution {
    public:
        int search(vector<int>& nums, int target) {
            int l = 0;
            int r = nums.size()-1;
            if(nums.size() == 0){
                return -1;
            }
    
            while (l <= r){
                int m = l + (r-l)/2;
                if(nums[m] == target){
                    return m;
                }
    
                if(nums[l] <= nums[m]){
                    if(target >= nums[l] && target <= nums[m]){
                        r = m-1;
                    }
                    else{
                        l = m+1;
                    }
                }
                else{
                    if(target >= nums[m] && target <= nums[r]){
                        l = m+1;
                    }
                    else{
                        r = m-1;
                    }
                }
            }
            return -1;
    
        }
    };
