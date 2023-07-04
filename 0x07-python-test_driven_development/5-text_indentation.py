#!/usr/bin/python3

"""
5-text_indentation module
edits a text.
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    args:
        text (str): the text to be printede.
    return: string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    character_list = list()
    splitted_text = list()
    new_text = list()
    for character in text:
        character_list.append(character)
        if character in [".", "?", ":"]:
            splitted_text.append(''.join(character_list))
            character_list.clear()
    if character_list:
        splitted_text.append(''.join(character_list))
    character_list.clear()
    for sentence in splitted_text:
        new_text.append(sentence.strip(" "))
    splitted_text.clear()
    for character in new_text[-1]:
        if character in [".", "?", ":"]:
            print("\n\n".join(new_text))
            print()
            return
    print("\n\n".join(new_text), end="")
