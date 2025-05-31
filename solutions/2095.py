from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        if size == 1:
            return None

        ptr = 0
        curr = head
        while curr:
            ptr += 1
            if ptr == int(size/2):
                curr.next = curr.next.next
            curr = curr.next
        return head

s = Solution()

l4=ListNode(val=4)
l3=ListNode(val=3, next=l4)
l2=ListNode(val=2, next=l3)
l1=ListNode(val=1, next=l2)

ll1=s.deleteMiddle(head=l1)
while ll1:
    print(ll1.val)
    ll1 = ll1.next
