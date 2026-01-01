/*
Problem: Two Sum
LeetCode: https://leetcode.com/problems/two-sum/
Topic: Hashing
Difficulty: Easy

Approach:
- Use unordered_map to store value -> index
- For each element, check if (target - current) exists

Comments: 
- map.find() does not return boolean, we have to compare map.find()with map.end()
- array in cpp is {}

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            unordered_map<int,int> mp;
            for(int i = 0; i < nums.size(); i++){
                if(mp.find(target-nums[i])!=mp.end()){
                    return {i, mp[target-nums[i]]};
                }
                mp[nums[i]] = i;
            }
            return {};
        }
    };
