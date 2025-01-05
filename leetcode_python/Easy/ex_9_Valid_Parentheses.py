class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Mapping of closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}

        # Iterate over the string
        for char in s:
            if char in bracket_map.values():  # If the character is an opening bracket
                stack.append(char)
            elif char in bracket_map:  # If the character is a closing bracket
                if stack and stack[-1] == bracket_map[char]:  # Check if top of stack matches the opening bracket
                    stack.pop()
                else:
                    return False  # Invalid if no matching opening bracket

        # The string is valid if the stack is empty at the end
        return not stack