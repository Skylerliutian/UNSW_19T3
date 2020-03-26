'''
>>> print(os.popen('echo "Please do my assignment..." | python3 roman_arabic.py').read(), end='')
How can I help you? I don't get what you want, sorry mate!

>>> print(os.popen('echo "please convert 35" | python3 roman_arabic.py').read(), end='')
How can I help you? I don't get what you want, sorry mate!

>>> print(os.popen('echo "Please convert 035" | python3 roman_arabic.py').read(), end='')
How can I help you? Hey, ask me something that's not impossible to do!

>>> print(os.popen('echo "Please convert 4000" | python3 roman_arabic.py').read(), end='')
How can I help you? Hey, ask me something that's not impossible to do!

>>> print(os.popen('echo "Please convert IIII" | python3 roman_arabic.py').read(), end='')
How can I help you? Hey, ask me something that's not impossible to do!

>>> print(os.popen('echo "Please convert IXI" | python3 roman_arabic.py').read(), end='')
How can I help you? Hey, ask me something that's not impossible to do!

>>> print(os.popen('echo "Please convert 35" | python3 roman_arabic.py').read(), end='')
How can I help you? Sure! It is XXXV

>>> print(os.popen('echo "Please convert 1982" | python3 roman_arabic.py').read(), end='')
How can I help you? Sure! It is MCMLXXXII

>>> print(os.popen('echo "Please convert 3007" | python3 roman_arabic.py').read(), end='')
How can I help you? Sure! It is MMMVII

>>> print(os.popen('echo "Please convert MCMLXXXII" | python3 roman_arabic.py').read(), end='')
How can I help you? Sure! It is 1982

>>> print(os.popen('echo "Please convert MMMVII" | python3 roman_arabic.py').read(), end='')
How can I help you? Sure! It is 3007

>>> print(os.popen('echo "Please convert 123 by using ABC" | python3 roman_arabic.py').read(), end='')
How can I help you? I don't get what you want, sorry mate!

>>> print(os.popen('echo "Please convert 123 ussing ABC" | python3 roman_arabic.py').read(), end='')
How can I help you? I don't get what you want, sorry mate!

>>> print(os.popen('echo "Please convert XXXVI using VI" | python3 roman_arabic.py').read(), end='')
How can I help you? Hey, ask me something that's not impossible to do!

>>> print(os.popen('echo "Please convert XXXVI using IVX" | python3 roman_arabic.py').read(), end='')
How can I help you? Hey, ask me something that's not impossible to do!

>>> print(os.popen('echo "Please convert XXXVI using XWVI" | python3 roman_arabic.py').read(), end='')
How can I help you? Hey, ask me something that's not impossible to do!

>>> print(os.popen('echo "Please convert I using II" | python3 roman_arabic.py').read(), end='')
How can I help you? Hey, ask me something that's not impossible to do!

>>> print(os.popen('echo "Please convert _ using _" | python3 roman_arabic.py').read(), end='')
How can I help you? Hey, ask me something that's not impossible to do!

>>> print(os.popen('echo "Please convert XXXVI using XVI" | python3 roman_arabic.py').read(), end='')
How can I help you? Sure! It is 36

>>> print(os.popen('echo "Please convert XXXVI using XABVI" | python3 roman_arabic.py').read(), end='')
How can I help you? Sure! It is 306

>>> print(os.popen('echo "Please convert EeDEBBBaA using fFeEdDcCbBaA" | python3 roman_arabic.py').read(), end='')
How can I help you? Sure! It is 49036

>>> print(os.popen('echo "Please convert 49036 using fFeEdDcCbBaA" | python3 roman_arabic.py').read(), end='')
How can I help you? Sure! It is EeDEBBBaA

>>> print(os.popen('echo "Please convert 899999999999 using AaBbCcDdEeFfGgHhIiJjKkLl" | python3 roman_arabic.py').read(), end='')
How can I help you? Sure! It is Aaaabacbdcedfegfhgihjikjlk

>>> print(os.popen('echo "Please convert ABCDEFGHIJKLMNOPQRST using AbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStT" | python3 roman_arabic.py').read(), end='')
How can I help you? Sure! It is 11111111111111111111

>>> print(os.popen('echo "Please convert 1900604 using LAQMPVXYZIRSGN" | python3 roman_arabic.py').read(), end='')
How can I help you? Sure! It is AMAZING

>>> print(os.popen('echo "Please convert ABCD minimally using ABCDE" | python3 roman_arabic.py').read(), end='')
How can I help you? I don't get what you want, sorry mate!

>>> print(os.popen('echo "Please convert ABCD minimaly" | python3 roman_arabic.py').read(), end='')
How can I help you? I don't get what you want, sorry mate!

>>> print(os.popen('echo "Please convert 0I minimally" | python3 roman_arabic.py').read(), end='')
How can I help you? Hey, ask me something that's not impossible to do!

>>> print(os.popen('echo "Please convert ABAA minimally" | python3 roman_arabic.py').read(), end='')
How can I help you? Hey, ask me something that's not impossible to do!

>>> print(os.popen('echo "Please convert ABCDEFA minimally" | python3 roman_arabic.py').read(), end='')
How can I help you? Hey, ask me something that's not impossible to do!

>>> print(os.popen('echo "Please convert MDCCLXXXVII minimally" | python3 roman_arabic.py').read(), end='')
How can I help you? Sure! It is 1787 using MDCLXVI

>>> print(os.popen('echo "Please convert MDCCLXXXIX minimally" | python3 roman_arabic.py').read(), end='')
How can I help you? Sure! It is 1789 using MDCLX_I

>>> print(os.popen('echo "Please convert MMMVII minimally" | python3 roman_arabic.py').read(), end='')
How can I help you? Sure! It is 37 using MVI

>>> print(os.popen('echo "Please convert VI minimally" | python3 roman_arabic.py').read(), end='')
How can I help you? Sure! It is 4 using IV

>>> print(os.popen('echo "Please convert ABCADDEFGF minimally" | python3 roman_arabic.py').read(), end='')
How can I help you? Sure! It is 49269 using BA_C_DEF_G

>>> print(os.popen('echo "Please convert ABCCDED minimally" | python3 roman_arabic.py').read(), end='')
How can I help you? Sure! It is 1719 using ABC_D_E
'''


if __name__ == '__main__':
    import doctest
    import os
    print('Test Start......')
    doctest.testmod()
    print('Test Done! If not show "Test Failed", you pass my test')
