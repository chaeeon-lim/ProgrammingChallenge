import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # get filtered string
        f = "".join(re.findall("[a-zA-Z0-9]+", s.lower()))
        
        # make them half and reverse one
        a_half = len(f)//2
        b_half = a_half if len(f) % 2 == 0 else a_half+1
        a = f[:a_half]
        b = "".join(reversed(f[b_half:]))
        
        # compare it
        for c1, c2 in zip(a, b):
            if a != b:
                return False
        
        return True



# test case
if __name__ == "__main__":
    testcase = [
        ["h","e","l","l","o"]
      , ["H","a","n","n","a","h"]
    ]
    expected = [
        ["o","l","l","e","h"]
      , ["h","a","n","n","a","H"]
    ]
    solver = Solution()
    for i, (t, g) in enumerate(zip(testcase, expected)):
        solver.reverseString(t)
        if t == g:
            print(f"#{i} correct")
        else:
            print(f"#{i} icorrect\n"
            , f"\tExptected: {g}\n"
            , f"\tgot {t}"
            )