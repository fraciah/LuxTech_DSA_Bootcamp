"""
Implement an algorithm using Python to determine if all characters in a string are unique.
True if all characters are unique and False if not all characters are unique
"""

class Sol:
    def unique(self, s):
        st_s = []

        for ch in s:
            if ch in st_s:
                return False
            else:
                st_s.append(ch)
        return True

print(Sol().unique(s = "abdddaacd"))