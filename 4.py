class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    cur = dummy
    carry = 0

    while l1 is not None or l2 is not None:
        if l1 is not None:
            x = l1.val
        else:
            x = 0

        if l2 is not None:
            y = l2.val
        else:
            y = 0

        total = x + y + carry
        cur.next = ListNode(total % 10)
        cur = cur.next
        carry = total // 10

        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next

    if carry != 0:
        cur.next = ListNode(carry)

    return dummy.next


if __name__ == "__main__":
    a = ListNode(9, ListNode(9))
    b = ListNode(1)
    res = addTwoNumbers(a, b)
    while res:
        print(res.val, end=" ")
        res = res.next
    print()