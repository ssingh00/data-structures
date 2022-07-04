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

        


class mergeLL:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ll = LinkedList()
        list1 = ll.convert_list_to_linkedlist(list1)
        list2 = ll.convert_list_to_linkedlist(list2)
        head = output = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                output.next = ListNode(list1.val)
                list1 = list1.next
            else:
                output.next = ListNode(list2.val)
                list2 = list2.next
            output = output.next
                
        output.next = list1 if list1 else list2
        return head.next

if __name__=="__main__":
    list1 = [1,2,4]
    list2 = [1,3,4]
    mll = mergeLL()
    f = mll.mergeTwoLists(list1, list2)
    lst  = []
    while f:
        lst.append(f.val)
        f = f.next
    print(lst)
