from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    L1 = put_into_int(l1)
    L2 = put_into_int(l2)
    c = list(str(L1+L2))

    i= len(c)-1
    l3= ListNode(int(c[i]))
    result= l3
    while i:          
        i-=1
        ch= int(c[i])
        if result != None:
            result.next= ListNode(ch)          
            result= result.next
    return l3
    
        
def put_into_int(l):
    s = ''
    while l:
        s = str(l.val)+s
        l = l.next
    return int(s)


l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
addTwoNumbers(l1,l2)