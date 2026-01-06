/*
Problem: Check if Array Is Sorted and Rotated
LeetCode: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
Topic: Array
Difficulty: Easy  

Approach:
- Count the number of times nums[i] < nums[i-1] occurs (inversions)
- Also check if the last element is greater than the first element (wraps around)
- For a sorted and rotated array, there should be at most 1 inversion
- If flag == 0, array is sorted (no rotation or full rotation)
- If flag == 1, array is sorted and rotated once
- If flag > 1, array is not sorted and rotated

Time Complexity: O(n)
Space Complexity: O(1)
*/



class Solution {
    public:
        bool check(vector<int>& nums) {
            int flag = 0;
            for(int i = 1; i < nums.size(); i++){
                if(nums[i] < nums[i-1]){
                    flag++;
                }
            }
            int x = nums.size();
            if(nums[x-1] > nums[0]){
                flag++;
            }
            if(flag == 0 || flag == 1){
                return true;
            }
            return false;
        }
    };
