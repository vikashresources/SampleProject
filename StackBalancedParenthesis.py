from Stack import Stack

''' () , ()() , {{{}}}

( )

{ }

{ }

}

'''


class StackBalancedParenthesis:

    def is_match(self, pop, paren):
        if pop == '(' and paren == ')':
            return True
        elif pop == '{' and paren == '}':
            return True
        elif pop == '[' and paren == ']':
            return True
        else:
            return False

    def is_parenthesis_balanced(self, pattern_string):
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
                    if not self.is_match(top, paren):
                        is_balanced = False

            index += 1

        if s.is_empty() and is_balanced:
            return True
        else:
            return False


if __name__ == '__main__':
    sbp = StackBalancedParenthesis()
    print(sbp.is_parenthesis_balanced('(())'))
    print(sbp.is_parenthesis_balanced('(()'))
    print(sbp.is_parenthesis_balanced('(({[]}))'))