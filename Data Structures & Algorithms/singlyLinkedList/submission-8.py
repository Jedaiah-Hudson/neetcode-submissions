class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        idx = 0
        while curr:
            if idx == index:
                return curr.val
            curr = curr.next
            idx += 1
        return -1

    def insertHead(self, val: int) -> None:
        newHead = ListNode(val)
        newHead.next = self.head
        self.head = newHead

        return
    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        if not self.head:
            self.head = newNode
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode
        return

    def remove(self, index: int) -> bool:
        #No head
        if not self.head:
            return False
        #if its the head
        if index == 0:
            if not self.head.next:
                self.head = None
                return True
            else:
                self.head = self.head.next
                return True
        

        idx = 0
        curr = self.head
        while curr:
            if (idx + 1) == index:
                if not curr.next:
                    return False

                curr.next = curr.next.next
                return True
            curr = curr.next
            idx += 1
        return False
        

    def getValues(self) -> List[int]:
        if not self.head:
            return []
        retArr = []
        curr = self.head
        while curr:
            retArr.append(curr.val)
            curr = curr.next
        return retArr
        
