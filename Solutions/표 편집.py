from collections import deque


class Node:
    def __init__(self, index):
        self.index = index
        self.prev = - 1
        self.next = - 1
        self.isdeleted = False


def solution(n, k, cmd):
    # answer 초기화
    answer = ''

    linked_list = [Node(i) for i in range(n)]

    deleted_buffer = deque()

    for node in linked_list:
        if node.index == 0:
            node.next = node.index + 1
        elif node.index == n - 1:
            node.prev = node.index - 1
        else:
            node.prev = node.index - 1
            node.next = node.index + 1

    index = k
    for c in cmd:
        if c == "C":
            if linked_list[index].next == - 1:
                deleted_buffer.append(index)
                linked_list[index].isdeleted = True
                linked_list[linked_list[index].prev].next = -1
                index = linked_list[index].prev
            else:
                deleted_buffer.append(index)
                linked_list[index].isdeleted = True
                left_index = linked_list[index].prev
                right_index = linked_list[index].next
                linked_list[left_index].next = right_index
                linked_list[right_index].prev = left_index
                index = linked_list[index].next
        elif c == "Z":
            recover = deleted_buffer.pop()
            linked_list[recover].isdeleted = False
            left_index = linked_list[recover].prev
            right_index = linked_list[recover].next
            if left_index != -1:
                linked_list[left_index].next = recover
            if right_index != -1:
                linked_list[right_index].prev = recover
        else:
            letter, num = c.split(' ')
            if letter == "U":
                for i in range(int(num)):
                    index = linked_list[index].prev
            else:
                for i in range(int(num)):
                    index = linked_list[index].next
    for node in linked_list:
        if node.isdeleted == False:
            answer += "O"
        else:
            answer += "X"
    return answer