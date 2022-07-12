# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def convert_list_to_linkedlist(self, lst):
        self.head = output = ListNode()
        i = 0  
        while i < len(lst):
            output.next = ListNode(lst[i])
            output = output.next
            i+=1
        return self.head.next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ll = LinkedList()
        list1 = ll.convert_list_to_linkedlist(head)
        curr = new = ListNode() 
        lst = set()
        while list1:
            if list1.val in lst:
                list1=list1.next
                continue
            else:
                lst.add(list1.val)
                new.next = ListNode(list1.val)
                list1 = list1.next
            new=new.next
                
        return curr.next

if __name__=="__main__":
    list1 = [1,1,4]

    sl = Solution()
    f = sl.deleteDuplicates(list1)
    lst  = []
    while f:
        lst.append(f.val)
        f = f.next
    print(lst)