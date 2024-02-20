def reverse_sentence(sentence):
    """
    Reverses a sentence words without reversing the letters in the words.

    argument:
    sentence: str: sentence to reverse

    returns:
    reversed_sentence: str: the reversed sentence
    """
    new_sentence_list = []
    
    for word in sentence.split(' '):
        new_sentence_list.insert(0,word)
    
    return " ".join(new_sentence_list)


my_sentence = "hello and welcome to the world of programmiing"
print(reverse_sentence(my_sentence))
