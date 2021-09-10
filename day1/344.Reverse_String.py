class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        half = len(s)//2
        for i in range(half):
            s[i], s[-(i+1)] = s[-(i+1)], s[i]


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
