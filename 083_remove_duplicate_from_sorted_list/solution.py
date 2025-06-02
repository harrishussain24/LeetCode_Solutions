class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if not head or not head.next:
            return head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else :
                current = current.next
        
        return head