class Solution:
    """Solution to restore IP addresses from a string"""
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, path):
            """Backtrack function to generate all possible IP addresses from the string s"""
            if start == len(s) and len(path) == 4:
                res.append('.'.join(path))
                return
            if len(path) == 4:
                return
            for i in range(1, 4):
                if start + i > len(s):
                    break
                if i > 1 and s[start] == '0':
                    break
                if int(s[start:start+i]) <= 255:
                    backtrack(start+i, path + [s[start:start+i]])
        res = []
        backtrack(0, [])
        return res
