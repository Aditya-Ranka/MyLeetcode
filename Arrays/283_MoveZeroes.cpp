/*
Problem: Move Zeroes
LeetCode: https://leetcode.com/problems/move-zeroes/description/
Topic: Array, Two Pointers
Difficulty: Easy  

Approach:
- Use two pointers: one to track the position for non-zero elements (k), one to iterate through the array (i)
- When we encounter a non-zero element, place it at position k and increment k
- After moving all non-zero elements to the front, fill the remaining positions with zeros
- This maintains the relative order of non-zero elements

Time Complexity: O(n)
Space Complexity: O(1)
*/




class Solution {
    public:
        void moveZeroes(vector<int>& nums) {
            int k = 0; //nonzero flag
            for (int i = 0; i < nums.size(); i++){
                if (nums[i] != 0){
                    nums[k] = nums[i];
                    k++;
                }
            }
    
            for(int j = k; j < nums.size(); j++){
                nums[j] = 0;
            }
        }
    };
    
    
