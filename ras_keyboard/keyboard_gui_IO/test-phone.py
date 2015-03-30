#-*- coding: utf-8 -*-
from phone import split_fins, assemble, PhoneAutomata

def assert_eq(x, y, unordered):
    xl = list(x)
    yl = list(y)
    if unordered:
        xl.sort()
        yl.sort()
    if len(xl) != len(yl):
        return False
    for i in range(len(xl)):
        if xl[i] != yl[i]:
            return False
    return True

def dump(u):
    if isinstance(u, list):
        return "".join(u)
    else:
        return u

def test(given, expected, comment="", unordered=False):
    if assert_eq(given, expected, unordered):
        print "PASS", comment
        return True
    else:
        print "FAIL", comment
        print "    given   ", dump(given)
        print "    expected", dump(expected)
        return False

def test_full_stack(string, result, FinFirst=True):
    p = PhoneAutomata(FinFirst)
    for c in list(string):
        if c in list("1234567890"):
            p.feed(c)
        elif c == " ":
            p.next()
        elif c == "\x7f":
            p.back()

    test(p.writer.dump(), result, result)

print ">>>>>>> 1. Helper functions >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
test(map(split_fins, ["","1111","1112222"]), [(),("1111",),("111","2222")], "split_fins()")

suite = u"""
    4444,,,ㄱ; 000,,,ㅇ;
    5,12,,나; 66,211,,테;
    7,12,554,밝; 888,3,,쓰; 999,21,557,쩗;
    0,32211,0,웽
"""
suite = map(lambda x: x.strip().split(","), suite.split(";"))
for case in suite:
    test(assemble(case[0],case[1],case[2]), case[3], "assemble "+case[3])

print ">>>>>>> 2. FinFirstWriter >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
suite = u"""
    41221,걔
    43412,그가
    61255,달
    612554,닭
    6125541,달기
    612554122,달갸
    61255412255,달걀
    0125,안
    01255,알
    012555,안
    0125558,안ㅅ
    01255588,않
    012555888,안ㅆ
    0125558888,안ㅅ
    777777732211554444,뷁
    8125,산
    81258,산ㅅ
    812583,산스
    8125832,산수
    02,ㅇ.
    023,오
    02312,와
    0231255,왈
    02312552,와ㄹ.
    023125522,와ㄹ..
    0231255223,와료
    02312552230,와룡
    51255,날
    51255 ,날
    51255 512,날나
    512555,난
    0124120122,아가야
    0124120122\x7f,아가
    0124120122\x7f\x7f,아
    0124120122\x7f\x7f031,아의
    456,ㄱㄴㄷ
    5121111,내ㅣㅣㅣ
    01256712,안ㄷ바
"""
for line in suite.split("\n"):
    if "," in line:
        string, result = line.strip().split(",")
        test_full_stack(string, result, True)

print ">>>>>>> 3. IniFirstWriter >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
suite = u"""
    41221,걔
    43412,그가
    61255,다ㄹ
    612554,달ㄱ
    6125541,달기
    612554122,달갸
    61255412255,달갸ㄹ
    61255412255 ,달걀
    0125,아ㄴ
    01255,아ㄹ
    012555,아ㄴ
    0125558,안ㅅ
    01255588,안ㅎ
    012555888,안ㅆ
    0125558888,안ㅅ
    777777732211554444,뷀ㄱ
    777777732211554444 ,뷁
    8125,사ㄴ
    81258,산ㅅ
    812583,산스
    8125832,산수
    02,ㅇ.
    023,오
    02312,와
    0231255,와ㄹ
    02312552,와ㄹ.
    023125522,와ㄹ..
    0231255223,와료
    02312552230,와료ㅇ
    02312552230 ,와룡
    51255,나ㄹ
    51255 ,날
    51255 512,날나
    512555,나ㄴ
    0124120122,아가야
    0124120122\x7f,아가
    0124120122\x7f\x7f,아
    0124120122\x7f\x7f031,아의
    456,ㄱㄴㄷ
    5121111,내ㅣㅣㅣ
    01256712,안ㄷ바
"""
for line in suite.split("\n"):
    if "," in line:
        string, result = line.strip().split(",")
        test_full_stack(string, result, False)



