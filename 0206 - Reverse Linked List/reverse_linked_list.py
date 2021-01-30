def reverseList(self, head):
    # 1 -> 2 -> 3 -> 4 -> 5 -> None
    # Keeps the previous node in memory. The head doesn't have a previous node
    prev = None

    # Checks if head exists (breaks when head is None)
    while head:
        # Variable to temporarily hold the value of head while we change head (1st iteration: temp = 1)
        temp = head
        # Moves the head on forward (1st iteration: 1 -> >>2<< -> 3 -> 4 -> 5 -> None)
        head = head.next
        # Changes the pointer of the temp node 1 to prev (changes direction) and points to None
        temp.next = prev
        # In the next iteration, prev is going to equal 1
        prev = temp
    return prev
    