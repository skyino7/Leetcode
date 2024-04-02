class Solution:
    def isValid(self, s: str) -> bool:
        charDict = {')':'(', '}':'{', ']':'['}
        stack = []

        for char in s:
            if char in charDict.values():
                stack.append(char)
            elif char in charDict.keys():
                if stack == [] or charDict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
