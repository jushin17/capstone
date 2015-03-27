# -*- encoding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui, uic
from getch import _Getch
from phone import PhoneAutomata

print u"""+------+------+------+
|  1   |  2   |  3   |
|  ㅣ  |  .   |  ㅡ  |
+------+------+------+
|  4q  |  5w  |  6e  |
|ㄱㅋㄲ| ㄴㄹ |ㄷㅌㄸ|
+------+------+------+
|  7a  |  8s  |  9d  |
|ㅂㅍㅃ|ㅅㅎㅆ|ㅈㅊㅉ|
+------+------+------+
| <BS> |  0x  | <SP> |
| DEL  | ㅇㅁ | NEXT |
+------+------+------+------+
| Press <BackSpace> delete. |
| Press <Space> to go next. |
+---------------------------+
"""

while True:
    print u"Enter '1' for 종성우선, '2' for 초성우선:",
    mode = raw_input("")
    if mode.startswith("1"):
        FinFirst = True
        break
    elif mode.startswith("2"):
        FinFirst = False
        break

keypad = {'1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '0':'0',
          'q':'4', 'w':'5', 'e':'6', 'a':'7', 's':'8', 'd':'9', 'x':'0'}

p = PhoneAutomata(FinFirst=FinFirst, debug=False)

getch = _Getch()
while True:
    c = getch()
    if c == "\x1b" or c == "\x03":
        print "\nbye."
        break
    elif c == " ":
        p.next()
    elif c == "\x7f":
        p.back()
    else:
        if c in keypad:
            p.feed(keypad[c])
    print "\r" + p.writer.dump() + " ",

