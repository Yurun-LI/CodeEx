class ListNode():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
class LinkNodes():
    def __init__(self,head=0,next=None):
        self.headNode = ListNode(head)
    def add(self,val):
        curr = self.headNode
        while curr.next is not None:
            curr = curr.next
        curr.next = ListNode(val = val)


test1 = LinkNodes()
test2 = LinkNodes()
l1 = [2,4,3]
l2 = [5,6,4]

for i,j in zip(l1,l2):
    test1.add(i)
    test2.add(j)



class Solution:
    def addTwoNumbers(self,l1:ListNode,l2:ListNode)->ListNode:
        resNum = self.linkNode_to_int(l1) + self.linkNode_to_int(l2)
        resNode = ListNode(val=resNum%10)
        resNum = resNum //10 
        curr = resNode
        while resNum != 0:
            curr.next = ListNode(val = resNum % 10)
            resNum = resNum //10
            curr = curr.next
        return resNode
    def linkNode_to_int(self,l:ListNode)->int:
        res = 0
        idx = 0
        curr = l
        while curr != None:
            res += curr.val*10**idx
            idx+=1
            curr = curr.next
        return res
