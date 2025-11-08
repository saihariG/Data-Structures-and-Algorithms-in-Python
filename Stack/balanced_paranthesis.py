class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, data):
        new_node = ListNode(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None

        popped = self.top.data

        self.top = self.top.next
        self.size -= 1

        return popped

    def peek(self):
        if self.is_empty():
            return None

        return self.top.data

#       Algorithm :
#       @return boolean
#       1. Define a Stack
#       2. scan the String and parse the brackets
#       3. if the bracket is left/opening bracket it means another bracket suppose to
#          complete it. keep pushing into the stack
#       4. if a right/closing bracket is encountered check if the top item in the stack matches its reverse Bracket
#       5. if it is not equal or if stack is empty , it means they are not balanced
#       6. After parsing , if the stack is empty , then brackets are balanced

def is_bracket_balanced(s):
    stack = Stack()

    for ch in s:

        reverse_bracket = get_reverse_bracket(ch)

        if ch == '(' or ch == '[' or ch == '{':
            stack.push(ch)
        elif stack.is_empty() or stack.pop() != reverse_bracket:
            return False

    return stack.is_empty()

def get_reverse_bracket(c):
    match c:
        case '(':
            return ')'
        case '[':
            return ']'
        case '{':
            return '}'
        case ')':
            return '('
        case '}':
            return '{'
        case ']':
            return '['

    return None


if __name__ == "__main__":

    test1 = "{([])}"
    test2 = "{([)}"
    test3 = "{([])"
    test4 = "{[()]}"

    print(is_bracket_balanced(test1))
    print(is_bracket_balanced(test2))
    print(is_bracket_balanced(test3))
    print(is_bracket_balanced(test4))