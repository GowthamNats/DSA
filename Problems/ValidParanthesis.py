def isValid(s: str) -> bool:
    stack = []
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        else:
            if not stack:
                return False
            if (i == ')' and stack[-1] == '(') or (i == '}' and stack[-1] == '{') or (i == ']' and stack[-1] == '['):
                stack.pop()
            else:
                return False
    
    return len(stack) == 0

print(isValid("""()[]{}"""))