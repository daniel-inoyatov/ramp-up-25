def longest_substring(s: str) -> str:
    best_start, best_len = 0, 1
    start = 0
    for i in range(1, len(s)):
        if (int(s[i]) % 2) != (int(s[i-1]) % 2):
            curr_len = i - start + 1
            if curr_len > best_len:
                best_len = curr_len
                best_start = start
        else:
            start = i

    return s[best_start : best_start + best_len]


print(longest_substring("225424272163254474441338664823"))
print(longest_substring("594127169973391692147228678476"))
print(longest_substring("721449827599186159274227324466"))
