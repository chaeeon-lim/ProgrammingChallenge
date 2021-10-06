# a = "dig1 8 1 5 1"
# b = "dig2 3 6"

# c = [a, b]

# print(sorted(c))


def reorderLogFiles(logs):
    def sorting_key(log):
        identifier, data = log.split(" ", 1)
        if data[0].isalpha():
            return (0, data, identifier)
        else:
            return (1,)

    return sorted(logs, key=sorting_key)

if __name__ == "__main__":
    logs = [
        ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"],
        ["1 n u", "r 527", "j 893", "6 14", "6 82"]
        ]
    expected = [
        ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"],
        ["1 n u","r 527","j 893","6 14","6 82"]
        ]


    for l, e in zip(logs, expected):
        results = reorderLogFiles(l)
        
        print(results)

        if len(e) == len(results):
            for i, (j, k) in enumerate(zip(e, results)):
                if k != j:
                    print(f"{i}) {j} != {k}")
                    break
        else:
            print("length not match")

