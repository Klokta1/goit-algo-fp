class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Функція для додавання вузла на початок списку
def push(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    head = new_node
    return head

# Функція для виведення списку
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

# Функція для реверсування списку
def reverseList(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next    # Зберігаємо посилання на наступний вузол
        current.next = prev         # Реверсуємо поточне посилання
        prev = current              # Переміщаємо 'prev' на поточний вузол
        current = next_node         # Переходимо до наступного вузла
    head = prev                     # Оновлюємо голову списку
    return head

# Функція для злиття двох відсортованих списків
def sortedMerge(a, b):
    if a is None:
        return b
    if b is None:
        return a

    if a.data <= b.data:
        result = a
        result.next = sortedMerge(a.next, b)
    else:
        result = b
        result.next = sortedMerge(a, b.next)
    return result

# Функція для розбиття списку на дві половини
def frontBackSplit(source):
    if source is None or source.next is None:
        front = source
        back = None
        return front, back

    slow = source
    fast = source.next

    # Рухаємо 'fast' на два вузли, 'slow' на один
    while fast:
        fast = fast.next
        if fast:
            slow = slow.next
            fast = fast.next

    # Розділяємо список на дві частини
    front = source
    back = slow.next
    slow.next = None
    return front, back

# Рекурсивна функція сортування злиттям
def mergeSort(head):
    if head is None or head.next is None:
        return head

    # Розділяємо список на дві половини
    front, back = frontBackSplit(head)

    # Рекурсивно сортуємо підсписки
    front = mergeSort(front)
    back = mergeSort(back)

    # Зливаємо відсортовані списки
    return sortedMerge(front, back)

# Функція для об'єднання двох відсортованих списків
def mergeTwoSortedLists(list1, list2):
    return sortedMerge(list1, list2)

if __name__ == '__main__':
    # Створюємо список: 5->10->15
    a = None
    a = push(a, 15)
    a = push(a, 20)
    a = push(a, 10)
    a = push(a, 5)

    print("Заданий список:")
    printList(a)

    # Реверсуємо список
    a = reverseList(a)
    print("Реверсований список:")
    printList(a)

    # Сортуємо список
    a = mergeSort(a)
    print("Відсортований список:")
    printList(a)

    # Створюємо другий відсортований список: 2->3->20
    b = None
    b = push(b, 25)
    b = push(b, 3)
    b = push(b, 2)
    b = mergeSort(b)

    # Об'єднуємо два відсортовані списки
    res = mergeTwoSortedLists(a, b)
    print("Об'єднаний відсортований список:")
    printList(res)
