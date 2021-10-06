
from collections import Counter

def groupAnagrams(strs):
    group = {}
    for word in strs:
        key = str(sorted(word))
        if key not in group.keys():
            group[key] = [word]
        else:
            group[key].append(word)

    return list(group.values())


if __name__ == "__main__":
    strs = [
        ["eat","tea","tan","ate","nat","bat"]
        ]
    expected = [
        [["bat"],["nat","tan"],["ate","eat","tea"]]
        ]


    for i, (s, e) in enumerate(zip(strs, expected)):
        results = groupAnagrams(s)
        
        print(results)

        # if Counter(*results) != Counter(*e):
        #     print(f"test case {i} wrong: {results} != {e}")
        # else:
        #     print(f"test case {i} correct")


