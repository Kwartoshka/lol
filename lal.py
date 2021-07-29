class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:

    sum_list = []
    next_num = 0
    # if len(l1) > len(l2):
    #     l1, l2 = l2, l1
    # while len(l1) < len(l2):
    #     l1.append(0)
    # num1 = l1.next
    # print(num1)
    # num2 = l2.next
    # print(num2)
    # while num1 is not None and num2 is not None:
    #     print(num1, num2)
    #     summa = num1 + num2 + next_num
    #     next_num = summa // 10
    #     current_num = summa % 10
    #     sum_list.append(current_num)
    #     num1 = l1.next
    #     num2 = l2.next
    # return sum_list


a = ListNode(3)
print(a.next)
print(a.next)
print(a.next)
