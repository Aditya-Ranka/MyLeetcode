/*
Problem: Two Sum II - Input Array Is Sorted
LeetCode: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
Topic: Array, Two Pointers, Binary Search
Difficulty: Medium  

Approach:
- Since the array is sorted, use two pointers: one at the start, one at the end
- If sum of two pointers equals target, return their indices (1-indexed)
- If sum is less than target, move left pointer right (increase sum)
- If sum is greater than target, move right pointer left (decrease sum)
- Continue until we find the pair

Time Complexity: O(n)
Space Complexity: O(1)
*/



class Solution {
    public:
        vector<int> twoSum(vector<int>& numbers, int target) {
            int r = numbers.size()-1;
            int l = 0;
            while(1==1){
                int currSum = numbers[l] + numbers[r];
                if(currSum == target){
                    return {l+1,r+1};
                }
                if(currSum > target){
                    r--;
                }
                else{
                    l++;
                }
            }
        }
    };
