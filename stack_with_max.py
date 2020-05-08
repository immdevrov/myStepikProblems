class Stack:
    def __init__(self):
        self._stack = []
        self.length = -1

    def push(self, item):
        self._stack.append(item)
        self.length += 1

    def pop(self):
        self.length -= 1
        return self._stack.pop(self.length + 1)

    def top(self):
        return self._stack[self.length]

class Stack_with_max:
    def __init__(self):
        self.stack = Stack()
        self.stack_maxes = Stack()

    def push(self, item):
        self.stack.push(item)
        prev_max = self.stack_maxes.top() if self.stack_maxes.length > -1 else 0
        self.stack_maxes.push(max(item, prev_max))

    def pop(self):
        self.stack_maxes.pop()
        return self.stack.pop()

    def max(self):
        return self.stack_maxes.top()


number_of_commands = int(input())
commands = []

for i in range(number_of_commands):
    commands.append(input().split(' '))

tested_stack = Stack_with_max()

for command_str in commands:
    if len(command_str) == 2:
        tested_stack.push(int(command_str[1]))
    else:
        if command_str[0] == 'pop':
            tested_stack.pop()
        if command_str[0] == 'max':
            print(tested_stack.max())
