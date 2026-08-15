/*
Problem: Linked List Cycle
LeetCode: https://leetcode.com/problems/linked-list-cycle/
Topic: Linked List
Difficulty: Easy

Approach:
- Floyd's tortoise & hare: slow moves 1 step, fast moves 2.
- If there's a cycle the fast pointer laps and meets slow; if fast hits the end there's no cycle.

Time Complexity: O(n)
Space Complexity: O(1)
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* fast = head;
        ListNode* slow = head;
        
        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
            if(slow == fast){
                return true;
            }
        }
        return false;
    }
};
