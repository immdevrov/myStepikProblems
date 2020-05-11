class MinHeap:
    def __init__(self):
        self.__heap = []
        self.__last_index = -1
        self.__changes = []

    def __parent_index(self, i: int) -> int:
        return (i - 1) // 2

    def __left_child_index(self, i: int) -> int:
        return (2 * i) + 1

    def __right_child_index(self, i: int) -> int:
        return (2 * i) + 2

    def __swap(self, a, b: int):
        self.__changes.append(f'{a} {b}')
        self.__heap[a] = self.__heap[a] + self.__heap[b]
        self.__heap[b] = self.__heap[a] - self.__heap[b]
        self.__heap[a] = self.__heap[a] - self.__heap[b]

    def changes(self):
        return self.__changes

    def H(self, i: int) -> int:
        # get item
        return self.__heap[i]

    def S(self, index, element: int):
        # set item
        if index > self.__last_index:
            self.__heap.append(element)
            self.__last_index += 1
            return
        self.__heap[index] = element

    def __sift_up(self, i: int):
        if i == 0:
            return
        p = self.__parent_index(i)
        if self.H(p) > self.H(i):
            self.__swap(i, p)
            self.__sift_up(p)

    def __sift_down(self, i: int):
        l = self.__left_child_index(i)
        r = self.__right_child_index(i)
        index_min = i
        if (l <= self.__last_index) and self.H(l) < self.H(index_min):
            index_min = l
        if (r <= self.__last_index) and self.H(r) < self.H(index_min):
            index_min = r
        if i != index_min:
            self.__swap(i, index_min)
            self.__sift_down(index_min)

    def insert(self, element):
        i = self.__last_index + 1
        self.S(i, element)
        ls = self.__left_sibling_index(i)
        if ls > 0 and self.H(ls) > element:
            element = self.H(ls)
            self.__swap(i, ls)
            self.__sift_down(ls)
        self.__sift_up(self.__last_index)

    def insert_full(self, list: list):
        self.__heap = list
        self.__last_index = len(list) - 1
        for i in range((self.__last_index + 1) // 2, -1, -1):
            self.__sift_down(i)
        return self.__heap

    def extract_min(self):
        min = self.H(0)
        self.S(0, self.H(self.__last_index))
        self.__last_index -= 1
        self.__sift_down(0)
        return min





n = 6
arr = [i for i in range(n, -1, -1)]

heap = MinHeap()

heap.insert_full(arr)

changes = heap.changes()

print(len(changes))

for ch in changes:
    print(ch)
