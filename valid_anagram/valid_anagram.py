"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

"""


def isAnagram(s: str, t: str) -> bool:
    my_list:list[str] = list(s)
    for letter in t:
        if letter in my_list:
            my_list.remove(letter)
        else:
            return False
    if my_list == []:
        return True
    return False

print(isAnagram("anagram", 'nagaram'))
print(isAnagram("cat", 'tap'))


def isAnagram_another(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

print(isAnagram_another("anagram", 'nagaram'))
print(isAnagram_another("cat", 'tap'))
