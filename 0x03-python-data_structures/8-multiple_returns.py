#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if not length:
        return (length, None)
    return (length, sentence[0])
