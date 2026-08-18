class Node:
    def __init__(self, data=''):
        self.data = data
        self.prev = None
        self.next = None


n, m = map(int, input().split())
s = input()

# 가상 head, tail
head = Node()
tail = Node()

head.next = tail
tail.prev = head

# 처음 문자열을 연결 리스트에 넣기
last = head

for ch in s:
    new_node = Node(ch)
    new_node.prev = last
    new_node.next = tail
    last.next = new_node
    tail.prev = new_node
    last = new_node

# 처음 위치는 맨 뒤
cursor = tail

for _ in range(m):
    command = input().split()

    if command[0] == 'L':
        # 맨 앞이면 무시
        if cursor.prev != head:
            cursor = cursor.prev

    elif command[0] == 'R':
        # 맨 뒤면 무시
        if cursor != tail:
            cursor = cursor.next

    elif command[0] == 'D':
        # cursor가 tail이면 삭제할 빵이 없음
        if cursor != tail:
            delete_node = cursor

            delete_node.prev.next = delete_node.next
            delete_node.next.prev = delete_node.prev

            # 삭제 후 cursor는 다음 위치를 가리킴
            cursor = delete_node.next

    elif command[0] == 'P':
        ch = command[1]

        new_node = Node(ch)

        # cursor 앞에 삽입
        new_node.prev = cursor.prev
        new_node.next = cursor

        cursor.prev.next = new_node
        cursor.prev = new_node


# 결과 출력
result = []

node = head.next

while node != tail:
    result.append(node.data)
    node = node.next

print(''.join(result))
