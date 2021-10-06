
def longestPalindrome(s: str) -> str:
# b a b a d
# ba ab ba ad
# bab aba bad
# baba abad
# babad
    subs = {0: [c for c in s]}
    pals = {0: s[0]}
    for i in range(1, len(s)):
        subs[i] = []
        for sub, c in zip(subs[i-1][:-1], s[i:]):
            word = sub+c
            subs[i].append(word)
            if (i%2==0 or i==1) and (sub[0] == c):
                pals[i] = word
            elif (i%2==1):
                if ((word[1]+word[0]) == word[-2:]):
                    pals[i] = word
    
    return list(pals.values())[-1]


if __name__ == "__main__":
    strs = [
        "babad",
        "bacab",
        "cbbd",
        "a",
        "ac",
        "aaaa",
        "aacabdkacaa",
        ]
    expected = [
        ["bab", "aba"],
        ["bacab"],
        ["bb"],
        ["a"],
        ["a", "cz"],
        ["aaaa"],
        ["aca"],
        ]

    for i, (s, e) in enumerate(zip(strs, expected)):
        results = longestPalindrome(s)
        
        print(results)
        if results in e:
            print(f"test case {i} correct")
        else:
            print(f"test case {i} wrong: {results} != {e}")

            
        # if Counter(*results) != Counter(*e):
        #     print(f"test case {i} wrong: {results} != {e}")
        # else:
        #     print(f"test case {i} correct")


