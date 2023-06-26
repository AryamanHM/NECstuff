from collections import Counter

def are_anagrams(str1, str2):
    # Compute the character frequencies for both strings
    freq1 = Counter(str1)
    freq2 = Counter(str2)

    # Compare the character frequencies
    return freq1 == freq2

# Test the function
string1 = "listen"
string2 = "silent"

if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
