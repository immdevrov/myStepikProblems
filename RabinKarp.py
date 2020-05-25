MOD_P = 1000000007
X_PARAM = 123

pattern = input()
text = input()

def plus(a, b, m):
    return (a % m + b % m) % m

def minus(a, b, m):
    return (a % m - b % m + m) % m

def multiply(a, b, m):
    return ((a % m) * (b % m)) % m

def p(a, b):
    return plus(a, b, MOD_P)

def m(a, b):
    return minus(a, b, MOD_P)

def x(a, b):
    return multiply(a, b, MOD_P)


x_powers = [1]
for i in range(1, len(text)):
    x_powers.append(x(x_powers[i-1], X_PARAM))


def hash(seq):
    res = 0
    for index, char in enumerate(seq):
        res = p(res, x(ord(char), x_powers[index]))
    return res % MOD_P


hash_pattern = hash(pattern)
remembered_power = x_powers[len(pattern) - 1]

last_hash = hash(text[len(text) - len(pattern):])
match = []
if last_hash == hash_pattern:
    if text[len(text) - len(pattern):] == pattern:
        match.append(str(len(text) - len(pattern)))

for i in range(len(text) - len(pattern) - 1, -1, -1):
    searching_seq = text[i:i + len(pattern)]
    last_char = ord(text[i + len(pattern)])
    rb_hash = p(
        x(m(last_hash, x(last_char, remembered_power)), X_PARAM), ord(text[i]))
    if rb_hash == hash_pattern:
        if searching_seq == pattern:
            match.append(str(i))
    last_hash = rb_hash

match.reverse()
print(' '.join(match))
