class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        """Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M."""
        roman = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}

        """Initialising the total to 0"""
        total = 0

        """Loop throught the string and check if the current element is in the roman dictionary"""
        for i in range(len(s)):
            """If the current element is in the roman dictionary,
            check if the next element is greater than the current element"""
            if s[i] in roman:
                if i + 1 < s and roman[s[i]] < roman[s[i + 1]]:
                    total -= roman[s[i]]
            else:
                total += roman[s[i]]
        """Return the total value of the roman numeral"""
        return total