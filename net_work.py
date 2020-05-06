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

# [size, n] = map(int, input().split(' '))
# arrival = []
# duration = []
# for i in range(n):
#   [a, d] = map(int, input().split(' '))
#   arrival.append(a)
#   duration.append(d)

queue = Queue()
queue.add('7')
queue.add('8')
queue.add('9')
print(queue.pop())
print(queue.pop())
print(queue.pop())
