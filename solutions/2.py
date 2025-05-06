from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # find highest count of l1 and l2 and store in `count`
        a_count = 0
        a = l1
        while a is not None:
            a_count += 1
            a = a.next


        b_count = 0
        b = l2
        while b is not None:
            b_count += 1
            b = b.next
    
        count = max(a_count, b_count)

        # add numbers in l1 and l2 and store in res_array
        res_array = []
        carry = 0
        c = l1
        d = l2
        sum = carry
        for i in range(count):
            if c is not None:
                sum += c.val

            if d is not None:
                sum += d.val

            # add numbers and store carry
            carry = sum // 10
            e = sum % 10

            res_array.append(ListNode(e))

            # reset
            c = c.next if c is not None else None
            d = d.next if d is not None else None
            sum = carry

        # if carry is not 0, add it to the end of res_array
        if carry != 0:
            res_array.append(ListNode(carry))

        # construct linked list from res_array
        res = ListNode(res_array[0].val)
        current = res
        for i in range(1, len(res_array)):
            current.next = ListNode(res_array[i].val)
            current = current.next

        return res



# l1 = [2,4,3]
# l2 = [5,6,4]
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
s = Solution()
res = s.addTwoNumbers(l1, l2)

# Output: [7,0,8,1]

# print res
current = res
while current is not None:
    print(current.val, end=" -> ")
    current = current.next
