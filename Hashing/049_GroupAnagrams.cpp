/*
Problem: Valid Anagram
LeetCode: https://leetcode.com/problems/group-anagrams/description/
Topic: Hashing
Difficulty: Medium

Approach:
-  Brute force would be sorting each string so for an array of m elements and n be the mean length of a string. 
-  O(m*nlogn) time complexity and O(m) space complexity. 

*better approach*
- a-z (26 letters
- HashMap: 
    (key, value) = (array of counts, list of anagrams)
    - key: array of 26 integers
    - value: list of anagrams

- Create a map like:
    Count array | All strings as a vec<string> 
- update counts properly using a nested loop. 
- push_back on mp[count] the string 
- exit the nested loop and outer loop
- create a vector<string called res
- push_back the strings in res from the map
- return res

Time Complexity: O(m*n)
Space Complexity: O(m)
*/


class Solution {
    public:
        vector<vector<string>> groupAnagrams(vector<string>& strs) {
            map<array<int, 26> , vector <string>> mp;
            for (string& s:strs){
                array <int, 26> count = {0};
                for(char c:s){
                    count[c - 'a']++;
                }
                mp[count].push_back(s);
            }
            vector <vector<string>> result;
            for(auto& p : mp){
                result.push_back(p.second);
            }
            return result;
        }
    };
