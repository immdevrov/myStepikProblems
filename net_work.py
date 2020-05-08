class Queue_item:
    def __init__(self, item, next, prev):
        self.value = item
        self.next = next
        self.prev = prev


class Queue:
    def __init__(self):
        self.length = 0
        self.last = None
        self.head = None

    def add(self, value):
        self.length += 1
        if self.length == 1:
            item = Queue_item(item=value, next=None, prev=None)
            self.head = item
            self.last = item
        else:
            last = self.last
            new_last = Queue_item(item=value, next=last, prev=None)
            self.last.prev = new_last
            self.last = new_last
            self.last.prev = None

    def pop(self):
        if self.length == 1:
            self.length = 0
            return self.head.value
        else:
            head = self.head
            self.head = self.head.prev
            self.head.next = None
            self.length -= 1
            return head.value


[size, n] = map(int, input().split(' '))
arrival = []
duration = []
handle_time = []
for i in range(n):
    [a, d] = map(int, input().split(' '))
    arrival.append(a)
    duration.append(d)
    handle_time.append(-1)

queue = Queue()


free_time = 0
time_of_first = 0

for i in range(n):
    if arrival[i] >= free_time:
        if queue.length < size:
            queue.add(i)
            handle_time[i] = max(arrival[i], time_of_first)
            time_of_first = handle_time[i] + duration[i]
        else:
            queue.pop()

print(handle_time)
