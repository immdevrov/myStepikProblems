n = int(input())
arr = list(map(int, input().split(' ')))
m = int(input())

befors = []
afters = []
max_of_window = []

for i in range(n):
    befors.append(0)
    afters.append(0)
    max_of_window.append(-1)


for i in range(n):
    if i % m != 0:
        befors[i] = max(arr[i], befors[i - 1])
    else:
        befors[i] = arr[i]

afters[n - 1] = arr[n - 1]
for j in range(n - 2, -1, -1):
    if (j + 1) % m != 0:
        afters[j] = max(arr[j], afters[j + 1])
    else:
        afters[j] = arr[j]

results = 0
for k in range(n - m + 1):
    max_of_window[k] = max(befors[k + m - 1], afters[k])
    results += 1

print(' '.join(map(str, filter(lambda x: x != -1, max_of_window))))
