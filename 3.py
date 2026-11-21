def lengthOfLongestSubstring(s):
    last_pos = {}     
    left = 0
    max_len = 0
    for right in range(len(s)):
        ch = s[right]

        if ch in last_pos:
            left = max(left, last_pos[ch] + 1)    

        last_pos[ch] = right

        max_len = max(max_len, right - left + 1)
    return max_len

if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))   
    print(lengthOfLongestSubstring("bbbbb"))      
    print(lengthOfLongestSubstring("pwwkew"))     
    print(lengthOfLongestSubstring("abba"))       