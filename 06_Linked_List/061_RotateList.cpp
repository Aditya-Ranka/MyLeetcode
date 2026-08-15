/*
Problem: Rotate List
LeetCode: https://leetcode.com/problems/rotate-list/
Topic: Linked List
Difficulty: Medium

Approach:
- Walk to the tail counting length, then close the list into a cycle (tail->next = head).
- Effective rotation is k % length; the new tail is (length - k%length) steps from the old tail.
- Step forward that many times, set new head = curr->next, then break the cycle (curr->next = NULL).

Time Complexity: O(L)
Space Complexity: O(1)
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if(head==NULL){
            return head;
        }
        ListNode* dummy = new ListNode;
        ListNode*curr = new ListNode;
        curr = head;
        int x = 1;
        while(curr->next){
            curr = curr->next;
            x++;
        }
        curr->next = head;
        int y = k%x;
        int z = x-y;
        for(int i = 0; i < z; i++){
            curr = curr->next;
        }
        dummy->next = curr->next;
        curr->next = NULL;
        return dummy->next;


    }
};
