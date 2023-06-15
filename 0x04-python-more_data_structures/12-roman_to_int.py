#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    converts a Roman numeral to an integer.
    Arguments:
        roman_string: a Roman numeral.
    Returns:
        converted Roman numeral.
    """
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    len_roman_str = len(roman_string)
    for i in range(len_roman_str):
        if roman_dic.get(roman_string[i], 0) == 0:
            return 0
        if (i != len_roman_str - 1) and (
           roman_dic[roman_string[i]] < roman_dic[roman_string[i + 1]]):
            number += roman_dic[roman_string[i]] * -1
        else:
            number += roman_dic[roman_string[i]]
    return number
