# Use these to test your is_palindrome function
test_strings = [
    "racecar",       # Standard palindrome
    "python",        # Not a palindrome
    "madam",         # Standard palindrome
    "hello",         # Not a palindrome
    "a",             # Single character (is a palindrome)
    "noon",          # Even-length palindrome
    "radar",         # Odd-length palindrome
    "algorithm",     # Not a palindrome
    "step on no pets" # Palindrome with spaces (advanced trick case!)
]

# Example of how to use it:
# for word in test_strings:
#     print(f"{word}: {is_palindrome(word)}")
def is_palindrome(s: str) -> bool:
    if not s:
        return True
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

for word in test_strings:
    print(f"{word}: {is_palindrome(word)}")