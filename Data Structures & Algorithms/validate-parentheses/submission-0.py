class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        b = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in b:
                # If closing bracket matches the most recent opening bracket, pop it
                if stack and stack[-1] == b[char]:
                    stack.pop()
                else:
                    return False
            else:
                # Store opening brackets on the stack
                stack.append(char)

        # Returns True if all nested pairs were matched and popped
        return len(stack) == 0