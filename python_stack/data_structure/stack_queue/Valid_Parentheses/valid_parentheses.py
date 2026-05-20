
def isValid(s: str) -> bool:
    """
    Checks if the input string of parentheses is valid.
    
    A string is valid if:
    1. Open brackets are closed by the same type of brackets.
    2. Open brackets are closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.
    
    Args:
        s (str): The string containing only the characters '(', ')', '{', '}', '[' and ']'.
        
    Returns:
        bool: True if the string is valid, False otherwise.
    """
    stack = []
    mapping = {
            ')': '(', 
            '}': '{', 
            ']': '[',
            }
    
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element: # ( != (
                return False
        else:
            stack.append(char)

    return len(stack) == 0

# Testcase
print(isValid("()"))        # Output: true
print(isValid("()[]{}"))    # Output: true
print(isValid("(]"))        # Output: false
print(isValid("([])"))      # Output: true
print(isValid("([)]"))      # Output: false
