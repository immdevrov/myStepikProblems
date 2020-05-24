X_M = 263
P_M = 1000000007

class Chain:
    def __init__(self):
        self._list = []

    def add(self, value):
        if self.is_exist(value):
            return
        self._list.insert(0, value)

    def rm(self, value):
        if self.is_exist(value):
            self._list.remove(value)

    def is_exist(self, value):
        return value in self._list

    def get(self):
        return ' '.join(self._list)


def hash(seq):
    res = 0
    for index, char in enumerate(seq):
        res += (ord(char) * ((X_M ** index) % P_M))
    return res % P_M

class HashTable:
    def __init__(self, m):
        self._table = [Chain() for _ in range(m)]
        self.m = m

    def add(self, string):
        h = hash(string) % self.m
        self._table[h].add(string)

    def rem(self, string):
        h = hash(string) % self.m
        self._table[h].rm(string)

    def find(self, string):
        h = hash(string) % self.m
        if self._table[h].is_exist(string):
            return 'yes'
        return 'no'

    def check(self, index):
        return self._table[index].get()

m = int(input())
n = int(input())
commands = []
for _ in range(n):
    commands.append(input().split(' '))

hash_table = HashTable(m)
for command, arg in commands:
    if command == 'add':
        hash_table.add(arg)
    if command == 'del':
        hash_table.rem(arg)
    if command == 'find':
        print(hash_table.find(arg))
    if command == 'check':
        print(hash_table.check(int(arg)))
