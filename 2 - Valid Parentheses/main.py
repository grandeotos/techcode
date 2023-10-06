class Solution:
    def isValid(self, s: str) -> bool:
        parent_stack = []  # The parenthesis stack
        close_open_hash = {
            ")": "(",
            "]": "[",
            "}": "{",
        }  # Hashmap used to convert the closing => opening brackets
        for char in s:  # Iterate over our characters
            if char in close_open_hash:
                if (parent_stack) and parent_stack[-1] == close_open_hash[char]:
                    parent_stack.pop()
                else:
                    return False
            else:
                parent_stack.append(char)
        return not parent_stack
