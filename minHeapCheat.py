
# n = int(input())
# arr = list(map(int, input().split(' ')))

n = 6
arr = [6, 5, 4, 3, 2, 1, 0]

d = {}
for i in range(n):
    d[arr[i]] = i

print(d)
s = sorted(d)
print(s)

# for el, j in enumerate(s) {
#     if el != d[j]:
#         print(f'{j} ')
# }


# print(len(changes))

# for ch in changes:
#     print(ch)
