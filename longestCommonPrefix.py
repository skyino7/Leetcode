class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        """Checking if the list is empty"""
        if not strs:
            return ""

        """Checking the first element in the string"""
        prefix = strs[0]

        """Iterating through the list and checking the common prefix"""
        for text in strs[1:]:
            while not text.startswith(prefix):
                prefix = prefix[:-1]
                if not strs:
                    return ""
        return prefix
