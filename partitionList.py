#partition a list with a given value T. all nodes with values smaller than T go before the node with values >= T. The original order of two parts should be preserved.
class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None
        
def partitionList(head, T):
    dummy = ListNode(0)
    dummy.next = head
    pre = p1 = dummy
    p0 = head

    while p0:
        if p0.val < T:
            #first cut p0 out
            pre.next = p0.next
            #insert p0 after p1, and move p1 to p0
            p1.next, p0.next, p1 = p0, p1.next, p0
            p0 = pre.next
        else:
            pre = p0
            p0 = p0.next
   #The swap
   #while p0:
   #    if p0.val < T:
   #        temp0 = p1.next.next
   #        temp1 = p1.next
   #        p1.next.next = p0.next
   #        p1.next = p0
   #        p1 = p0
   #        pre.next = temp1
   #        pre = temp1
   #        p0.next, p0 = temp0, p0.next
   #    else:
   #        pre = p0
   #        p0 = p0.next
    return dummy.next
    
def genListRand(L):
    import random
    p = dummy = ListNode(0)
    for i in range(L):
        p.next = ListNode(random.randint(1, 100))
        p = p.next
    return dummy.next

def genList(L):
    import random
    p = dummy = ListNode(0)
    for n in L:
        p.next = ListNode(n)
        p = p.next
    return dummy.next

def printList(head):
    i = 0
    while head:
        print("i:{} val:{}".format(i, head.val))
        head = head.next
        i += 1

if __name__ == "__main__":
    head = genList(list(range(5, 0, -1)))
    printList(head)
    head = partitionList(head, 3)
    print("---------")
    printList(head)
    
    