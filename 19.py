def wordBreak(s, wordDict):
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]
if __name__ == "__main__":
    cases = [
        ("leetcode", ["leet","code"], True),
        ("leetcode", ["leet","cod"], False),
        ("aaaaab", ["aa","aaaa","aaab"], True),
        ("catsanddog", ["cats","dog","sand","and","cat"], True),
        ("catsandog", ["cats","dog","sand","and","cat"], False),
        ("aaaa", ["a"], True),
        ("apple", ["apple"], True),
        ("a", ["a"], True),
        ("a", ["b"], False),
        ("ab", ["a","abc"], False),
        ("aa", ["a","a"], True),
        ("", ["a"], True),
    ]
    for i, (s, words, want) in enumerate(cases, 1):
        got = wordBreak(s, words)
        print(f"#{i}", "✅" if got == want else f"❌ 期望 {want} 实际 {got}")