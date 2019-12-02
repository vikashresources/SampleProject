from Stack import Stack

''' () , ()() , {{{}}}

( )

{ }

{ }

}



'''


def is_match(pop, paren):
    if pop == '(' and paren == ')':
        return True
    elif pop == '{' and paren == '}':
        return True
    elif pop == '[' and paren == ']':
        return True
    else:
        return False


def is_parenthesis_balanced(pattern_string):
    s = Stack()
    is_balanced = True
    index = 0
    while index < len(pattern_string) and is_balanced:
        paren = pattern_string[index]
        if paren in "{[(":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
    index += 1

    if s.empty() and is_balanced():
        return True
    else:
        return False


print(is_parenthesis_balanced("()"))
