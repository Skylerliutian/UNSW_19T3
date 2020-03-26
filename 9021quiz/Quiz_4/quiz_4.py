# COMP9021 19T3 - Rachid Hamadi
# Quiz 4 *** Due Thursday Week 5
#
# Prompts the user for an arity (a natural number) n and a word.
# Call symbol a word consisting of nothing but alphabetic characters
# and underscores.
# Checks that the word is valid, in that it satisfies the following
# inductive definition:
# - a symbol, with spaces allowed at both ends, is a valid word;
# - a word of the form s(w_1,...,w_n) with s denoting a symbol and
#   w_1, ..., w_n denoting valid words, with spaces allowed at both ends
#   and around parentheses and commas, is a valid word.


import sys
import re


def is_valid(word, arity):
    if arity == 0:
        if '(' in word or ')' in word:
            return False
        else:
            if '_' in word:
                word = word.replace('_', '')
            if word.isalpha():
                return True
            else:
                return False
    else:
        if word.count('(') != word.count(')'):
            return False
        else:
            if word.count('(') == 0:
                return False
            word = word.replace('_', '')
            symbol_list = re.split(r'[(),]', word)
            # print(symbol_list)
            # print(word)
            for i in range(len(symbol_list)):
                symbol_list[i] = symbol_list[i].strip()
            while '' in symbol_list:
                symbol_list.remove('')
            # print(symbol_list)
            if not all(s.isalpha() for s in symbol_list):
                return False
            else:
                word = word.replace(' ', '')
                punctuation_list = []
                for i in word:
                    if not i.isalpha():
                        punctuation_list.append(i)
                # print(punctuation_list)
                check_list = []
                for i in punctuation_list:
                    if i != ')':
                        check_list.append(i)
                    else:
                        check_list.append(i)
                        count_comma = 0
                        for j in check_list[::-1]:
                            if j == ',':
                                count_comma += 1
                            if j == '(':
                                break
                        if count_comma + 1 != arity:
                            return False
                        for _ in range(count_comma + 2):
                            check_list.pop()
                if len(check_list) == 0:
                    return True
                else:
                    return False






# REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE

try:
    arity = int(input('Input an arity : '))
    if arity < 0:
        raise ValueError
except ValueError:
    print('Incorrect arity, giving up...')
    sys.exit()
word = input('Input a word: ')
if is_valid(word, arity):
    print('The word is valid.')
else:
    print('The word is invalid.')
