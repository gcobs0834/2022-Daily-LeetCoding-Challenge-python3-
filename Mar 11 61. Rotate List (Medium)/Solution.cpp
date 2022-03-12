// O(N) | O(1)
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next) return head;
        int length = 1;
        ListNode* curr = head;
        while (curr->next){
            length++;
            curr = curr->next;
        }
        curr->next = head;
        
        k %= length;
        int lengthPrev = length - k - 1;
        curr = head;
        for (int i = 0; i < lengthPrev; i++){
            curr = curr->next;
        }
        ListNode* res = curr->next;
        curr->next = nullptr;
        return res;
    }
};
