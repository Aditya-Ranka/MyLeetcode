/*
Problem: Contains Duplicate
LeetCode: https://leetcode.com/problems/contains-duplicate/description/
Topic: Hashing
Difficulty: Easy

Approach:
- Use unordered_set


Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> set;
        for (int i = 0; i < nums.size(); i++){
            if(set.find(nums[i])!=set.end()){
                return true;
            }
            else{
                set.insert(nums[i]);
            }
        }
        return false;
    }
};
