class Solution:
    def isValid(self, s: str) -> bool:

        parentheses_stack = []

        opening_parentheses = ['(', '{', '[']
        closing_parentheses = [')', '}', ']']

        for c in s:
            if c in opening_parentheses:
                parentheses_stack.append(c)
            elif c in closing_parentheses:

                if len(parentheses_stack) == 0:
                    return False

                temp = parentheses_stack.pop()
                is_found_pair = False
                for i in range(3):
                    if temp == opening_parentheses[i] and c == closing_parentheses[i]:
                        is_found_pair = True

                if not is_found_pair:
                    return False

        if len(parentheses_stack) == 0:
            return True

        return False
