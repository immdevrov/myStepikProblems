def is_valid(seq):
    index = 0
    stack = []
    stack_indexes = []
    for c in seq:
        index += 1
        if c in '[({})]':
            if c in '({[':
                stack.append(c)
                stack_indexes.append(index)
            else:
                if len(stack) == 0:
                    return index
                top = stack.pop()
                if (top == '[' and c != ']') or (top == '(' and c != ')') or (top == '{' and c != '}'):
                    return index
                stack_indexes.pop()
    return 'Success' if len(stack) == 0 else stack_indexes[0]

statement = input()
print(is_valid(statement))
