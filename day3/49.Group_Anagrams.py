
from collections import Counter, deque

def groupAnagrams(strs):
    print(strs)
    group_anagram = [[strs[0]]]

    for word in strs[1:]:
        flag = True
        for group in group_anagram:
            print(f"{word} vs. {group}")
            if Counter(group[0]) == Counter(word):
                print(f"add {word} => {group}")
                group.append(word)
                flag = False
        if flag:
            print(f"new group for {word}")
            group_anagram.append([word])
                # print(group_anagram)
            # break

    # print(group_anagram)



    # anagrams = [[strs[0]]]
    # new = True
    # for word in strs[1:]:
    #     for a in anagrams:
    #         if set(word) == set(a[0]):
    #             a.append(word)
    #             new = False
    #     if new:
    
            
    return group_anagram
    # return []
                

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

        if Counter(*results) != Counter(*e):
            print(f"test case {i} wrong: {results} != {e}")
        else:
            print(f"test case {i} correct")


