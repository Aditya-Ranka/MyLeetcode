/*
Problem: Binary Search
LeetCode: https://leetcode.com/problems/binary-search/description/
Topic: Binary Search
Difficulty: Easy

Approach:
- Basic Basic Binary Search Algorithm. 



Time Complexity: O(logn)
Space Complexity: O(1) if we don't consider the space for the output array. 
*/


class Solution {
    public:
        int search(vector<int>& nums, int target) {
            int l = 0;
            int r =  nums.size() -1;
            
            while(l <= r){
                int m = l + (r-l)/2;
                if(nums[m] == target){
                    return m;
                }
                if(nums[m] < target){
                    l = m + 1;
                }
                else{
                    r = m-1;
                }
            }
            return -1;
        }
    };
