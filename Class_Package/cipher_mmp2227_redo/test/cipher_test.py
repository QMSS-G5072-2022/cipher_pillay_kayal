#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
    
def cipher_word_test():
    example = "lost"
    expected = "qtxy"
    actual = cipher(example, 3)
    assert actual == example

    print("Passed single word test. Yay!")

