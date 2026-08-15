/*
Problem: Remove Duplicates from Sorted Array
LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
Topic: Array, Two Pointers
Difficulty: Easy  

Approach:
- Use two pointers: one to track the position for unique elements, one to iterate through the array
- Since the array is sorted, duplicates will be adjacent
- When we encounter a new unique element (different from the previous), place it at the unique position
- Increment the unique position pointer
- Return the length of the unique portion of the array

Time Complexity: O(n)
Space Complexity: O(1)
*/


class Solution {
    public:
        int removeDuplicates(vector<int>& nums) {
            int a,k,c;
            c = -100000000000;
            k = 0;
            for (int num: nums){
                if (num > c){
                    nums[k] = num;
                    k++;
                    c = num;
                }
            }
            return k;
        }
    };
