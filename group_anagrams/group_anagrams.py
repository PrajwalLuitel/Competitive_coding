"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    grouped_anagrams:list[list[str]] = [[strs[0]]]

    for word in strs[1:]:
        count:int = 0
        for anagrams in grouped_anagrams:
            if sorted(anagrams[0]) == sorted(word):
                anagrams.append(word)
                count = 1
        
        if count == 0:
            grouped_anagrams.append([word])

    return grouped_anagrams


def groupAnagramsAgain(strs: list[str]) -> list[list[str]]:
    anagrams:dict[str:list[str]] = {}
    
    for word in strs:
        sorted_word:str = str(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    return anagrams.values()

def groupAnagramsAgainAgain(strs):
    anagrams:dict[tuple:list[str]] = {}

    for word in strs:
        counter:list[int] = [0]*26
        for character in word:
            counter[ord(character)-ord("a")] += 1
        counter = tuple(counter)
        try:
            anagrams[counter].append(word)
        except KeyError:
            anagrams[counter] = [word]

    return anagrams.values()


print(groupAnagramsAgainAgain(["eat","tea","tan","ate","nat","bat"]))