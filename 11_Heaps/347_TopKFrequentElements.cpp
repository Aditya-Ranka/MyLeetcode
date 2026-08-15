/*
Problem: Top K Frequent Elements
LeetCode: https://leetcode.com/problems/top-k-frequent-elements/
Topic: Heaps
Difficulty: Medium

Approach:
- Count frequencies in a hash map.
- Bucket sort by frequency: buckets[f] holds all values seen f times (max frequency is n).
- Walk buckets from high frequency down, collecting until k values are gathered.
- Avoids the O(n log n) of a heap/sort.

Time Complexity: O(n)
Space Complexity: O(n)
*/

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        for(int i = 0; i < nums.size(); i++){
            mp[nums[i]]++;
        }
        vector<vector<int>> buckets(nums.size()+1);
        for(auto& [val,cnt]: mp){
            buckets[cnt].push_back(val);
        }
        vector<int> res;
        for(int i = nums.size(); i>=1 && res.size() < k; i--){
            for(int val : buckets[i]){
                res.push_back(val);
                if(res.size() == k){
                    break;
                }
            }
        }
        return res;
    }
};
