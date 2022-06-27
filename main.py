class Stack:

    def __init__(self):
        self.list = []

    def isEmpty(self):
        return len(self.list) == 0

    def push(self, new_item):
        self.list.append(new_item)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[-1]

    def size(self):
        return len(self.list)


def check_balance(s):
    stack = Stack()
    opening_bracket = ['(', '{', '[']
    closing_bracket = [')', '}', ']']

    if len(s) % 2 > 0:
        return 'Несбалансированно'

    for bracket in s:
        if bracket in opening_bracket:
            stack.push(bracket)
        if bracket in closing_bracket:
            if len(stack.list) == 0:
                return 'Несбалансированно'
            i = closing_bracket.index(bracket)
            opening = opening_bracket[i]
            if stack.list[-1] == opening:
                stack.pop()
            else:
                return 'Несбалансированно'
    return 'Сбалансированно'


balanced = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}']
not_balanced = ['}{}', '{{[(])]}}', '[[{())}]']

if __name__ == "__main__":
    for i in balanced + not_balanced:
        print(check_balance(i))
