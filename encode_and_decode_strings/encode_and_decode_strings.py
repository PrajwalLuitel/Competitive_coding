"""
design an algorithm to encode a list of strings to a string. The encoded list is then sent over the network and decoded back.

Please implement encode and decode.

Example:
Example1:
Input: ["lint", "code", "love", "you"]
Output: ["lint", "code", "love", "you]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
"""


def encode(strs:list[str]):
    return "*#--#*".join(strs)

def decode(str:str):
    return str.split("*#--#*")

list_of_strs = ["Hello", "this", "is", "*##", "--#*", "world"]

print(f"encoded: {encode(list_of_strs)}")
print(f"decoded: {decode(encode(list_of_strs))}")
