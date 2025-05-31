from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lstz = []
        curr = head
        while curr:
            lstz.append(curr.val)
            curr = curr.next

        maxx = 0
        a=0
        b=len(lstz)-1
        while a < len(lstz):
            maxx=max(maxx,lstz[a]+lstz[b])
            a+=1
            b-=1

        return maxx

s = Solution()
l4=ListNode(val=4)
l3=ListNode(val=3, next=l4)
l2=ListNode(val=6, next=l3)
l1=ListNode(val=1, next=l2)

print(s.pairSum(head=l1))
