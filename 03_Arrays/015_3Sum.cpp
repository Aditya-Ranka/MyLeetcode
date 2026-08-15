/*
Problem: 3Sum
LeetCode: https://leetcode.com/problems/3sum/description/
Topic: Two Pointers
Difficulty: Medium

Approach:
- We break down this problem like wise: 
- first we sort this array (O(nlogn))
- now we run a loop over all possible a's
- now for each a we run a nested 2 sum sorted approach (O(n))
- we use two pointers to find the other two numbers that sum to -a
- if the sum is 0, we add the triplet to the result
- if the sum is less than 0, we move the left pointer to the right
- if the sum is greater than 0, we move the right pointer to the left
- we skip over duplicates by checking if the current element is the same as the previous element
- we return the result




Time Complexity: O(n^2)
Space Complexity: O(1) if we don't consider the space for the output array. 
*/



class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end()); 
        vector<vector<int>> arr;
        for (int i = 0; i < nums.size(); i++){
            if (i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            int a = nums[i];
            int l = i+1;
            int r = nums.size()-1;
            while(l < r){
                int currSum = nums[l] + nums[r] + a;
                if(currSum == 0){
                    arr.push_back({nums[i], nums[l], nums[r]});
                    while (l < r && nums[l] == nums[l + 1]) l++;
                    while (l < r && nums[r] == nums[r - 1]) r--;

                    l++;
                    r--;
                }
                else if(currSum < 0){
                    l++;
                }
                else{
                    r--;
                }
            }
            
        }
        return arr;
    }
};
