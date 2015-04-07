#-*- coding: utf-8 -*-
from dfa import DFA
from enfa import ENFAToDFAConverter
from regex import RegexParser
from mealy import Mealy
import copy

parser = RegexParser()
def get_dfa(reg_expr):
    global parser
    enfa = parser.parse(reg_expr)
    dfa = ENFAToDFAConverter(enfa).convert()
    dfa.minimize()
    return dfa

def split_fins(f):
    """
    '' -> ()
    '11111' -> ('11111')
    '11222' -> ('11', '222')
    """
    if len(f) == 0:
        return ()
    elif f[0] == f[-1]:
        return (f,)
    else:
        first = f[0]
        pos = f.count(first)
        return (f[:pos], f[pos:])

def assemble(i, m, f):
    def cycle_lookup(s):
        cycle = assemble.i_table[s[0]]
        pos = (len(s) - 1) % len(cycle)
        return cycle[pos]

    if len(i) == 0:
        i_char = ""
    else:
        i_char = cycle_lookup(i)

    if len(m) == 0:
        m_char = ""
    else:
        m_char = assemble.m_table[m]
        if m_char == "." or m_char == "..":
            return i_char + m_char

    f = split_fins(f)
    if len(f) == 0:
        f_char = ""
    elif len(f) == 1:
        f_char = cycle_lookup(f[0])
    else:
        f_char = cycle_lookup(f[0]) + cycle_lookup(f[1])

    if i_char == "":
        return m_char
    else:
        i_idx = assemble.i_list.index(i_char)

    if m == "":
        return i_char
    else:
        m_idx = assemble.m_list.index(m_char)

    f_idx = assemble.f_list.index(f_char)

    code = 44032 + 588 * i_idx + 28 * m_idx + f_idx
    return unichr(code)
assemble.i_table = {
    "4": u"ㄱㅋㄲ", "5": u"ㄴㄹ", "6": u"ㄷㅌㄸ",
    "7": u"ㅂㅍㅃ", "8": u"ㅅㅎㅆ", "9": u"ㅈㅊㅉ",
    "0": u"ㅇㅁ"
}
assemble.raw_m_table = u"""
    12:ㅏ, 122:ㅑ, 121:ㅐ, 1221:ㅒ,
    21:ㅓ, 221:ㅕ, 211:ㅔ, 2211:ㅖ,
    3:ㅡ, 31:ㅢ, 23:ㅗ, 231:ㅚ, 32:ㅜ, 321:ㅟ,
    1:ㅣ, 2:., 223:ㅛ, 322:ㅠ, 22:..,
    2312:ㅘ, 3221:ㅝ, 23121:ㅙ, 32211:ㅞ
"""
assemble.m_table = dict(map(lambda x: x.strip().split(":"), assemble.raw_m_table.split(",")))
assemble.i_list = u"ㄱ,ㄲ,ㄴ,ㄷ,ㄸ,ㄹ,ㅁ,ㅂ,ㅃ,ㅅ,ㅆ,ㅇ,ㅈ,ㅉ,ㅊ,ㅋ,ㅌ,ㅍ,ㅎ".split(",")
assemble.m_list = u"ㅏ,ㅐ,ㅑ,ㅒ,ㅓ,ㅔ,ㅕ,ㅖ,ㅗ,ㅘ,ㅙ,ㅚ,ㅛ,ㅜ,ㅝ,ㅞ,ㅟ,ㅠ,ㅡ,ㅢ,ㅣ".split(",")
assemble.f_list = u",ㄱ,ㄲ,ㄱㅅ,ㄴ,ㄴㅈ,ㄴㅎ,ㄷ,ㄹ,ㄹㄱ,ㄹㅁ,ㄹㅂ,ㄹㅅ,ㄹㅌ,ㄹㅍ,ㄹㅎ,ㅁ,ㅂ,ㅂㅅ,ㅅ,ㅆ,ㅇ,ㅈ,ㅊ,ㅋ,ㅌ,ㅍ,ㅎ".split(",")


def add_transition(R, A, p, x, q, function):
    """
    Add transition rules R(p,s) => state
    and mealy actions A(p,s) => function
    for all p in fromList and s in symList.

    fromList and symList are strings where each character
    represents a state or a symbol.
    """
    tmpR = R.get(p, {})
    tmpA = A.get(p, {})
    tmpR[x] = q
    tmpA[x] = function
    R[p] = tmpR
    A[p] = tmpA


def get_mealy(writer):
    R = {}
    A = {}

    add_transition(R, A, "S", "goodc", "I", writer.new_ini)
    add_transition(R, A, "S", "badv", "S", writer.bad_mid)
    add_transition(R, A, "I", "goodc", "I", writer.update_ini)

    add_transition(R, A, "I", "goodv", "M", writer.new_mid)
    add_transition(R, A, "I", "badc", "I", writer.bad_ini)
    add_transition(R, A, "M", "goodv", "M", writer.update_mid)
    add_transition(R, A, "M", "badv", "S", writer.bad_mid)

    add_transition(R, A, "M", "goodc", "F", writer.new_fin)
    add_transition(R, A, "F", "goodc", "F", writer.complex_fin)
    add_transition(R, A, "F", "badc", "I", writer.new_ini)
    add_transition(R, A, "F", "goodv", "M", writer.new_mid)

    add_transition(R, A, "F", "goodc2", "F2", writer.split_fin)
    add_transition(R, A, "F2", "goodc2", "F2", writer.split_fin)
    add_transition(R, A, "F2", "goodc", "F", writer.complex_fin)
    add_transition(R, A, "F2", "goodv", "M", writer.split_and_new_mid)
    add_transition(R, A, "F2", "badc", "I", writer.bad_fin)

    add_transition(R, A, "S", "next", "S", writer.abort)
    add_transition(R, A, "I", "next", "S", writer.abort)
    add_transition(R, A, "M", "next", "S", writer.abort)
    add_transition(R, A, "F", "next", "S", writer.abort)
    add_transition(R, A, "F2", "next", "S", writer.abort)

    d = {
        "states": ["S","I","M","F","F2"],
        "symbols": ["goodc", "goodv", "goodc2", "badc", "badv", "next"],
        "rules": R,
        "actions": A,
        "initial": "S",
    }
    return Mealy(d)

class FinFirstWriter:
    def __init__(self):
        self.i = ""
        self.m = ""
        self.f = ""
        self.f1 = ""
        self.f2 = ""
        self.text = ""
        self.last = ""

    def set_last_symbol(self, symbol):
        self.last = symbol

    def dump(self):
        d  = self.text + assemble(self.i, self.m, self.f)
        if self.f != self.f1 + self.f2:
            d += assemble(self.f2, "", "")
        # d += "(%s,%s,%s,%s)"%(self.i, self.m, self.f1, self.f2)
        return d

    def flush(self):
        self.text += assemble(self.i, self.m, self.f)
        self.i = ""
        self.m = ""
        self.f = ""
        self.n = ""
        self.f1 = ""
        self.f2 = ""

    def new_ini(self, command):
        self.flush()
        self.i = self.last

    def bad_ini(self, command):
        self.flush()
        self.i = self.last

    def update_ini(self, command):
        self.i += self.last

    def bad_mid(self, command):
        self.flush()
        self.m = self.last
        self.flush()

    def new_mid(self, command):
        tmp = split_fins(self.f)
        if len(tmp) == 1:
            self.f = ""
            self.flush()
            self.i = tmp[0]
        if len(tmp) == 2:
            self.f = tmp[0]
            self.flush()
            self.i = tmp[1]
        self.m = self.last

    def update_mid(self, command):
        self.m += self.last

    def new_fin(self, command):
        self.f1 = self.last
        self.f2 = ""
        self.f = self.f1

    def complex_fin(self, command):
        if self.f1[-1] == self.last:
            self.f1 += self.last
            self.f = self.f1
        else:
            self.f2 += self.last
            self.f = self.f1 + self.f2

    def split_fin(self, command):
        if self.f1[-1] == self.last:
            self.f1 += self.last
            self.f = self.f1
        else:
            self.f2 += self.last
            self.f = self.f1

    def bad_fin(self, command):
        if self.f2 != "":
            tmp = self.f2
        else:
            tmp = self.f1
        self.flush()
        self.i = tmp
        self.flush()
        self.i = self.last

    def split_and_new_mid(self, command):
        if len(self.f2) > 0:
            tmp = self.f2
        else:
            tmp = self.f1
        self.flush()
        self.i = tmp
        self.m = self.last

    def abort(self, command):
        self.flush()

    def back(self):
        self.flush()
        if len(self.text) > 0:
            self.text = self.text[:-1]

class IniFirstWriter:
    def __init__(self):
        self.i = ""
        self.m = ""
        self.f = ""
        self.n = ""
        self.f1 = ""
        self.f2 = ""
        self.text = ""
        self.last = ""
        self.should_split_fin = False

    def set_last_symbol(self, symbol):
        self.last = symbol

    def dump(self):
        d  = self.text + assemble(self.i, self.m, self.f) + assemble(self.n, "", "")
        #d += "(%s,%s,%s,%s|%s,%s)"%(self.i, self.m, self.f1, self.f2, self.f, self.n)
        return d

    def flush(self):
        self.text += assemble(self.i, self.m, self.f)
        self.i = self.n
        self.m = ""
        self.f = ""
        self.n = ""
        self.f1 = ""
        self.f2 = ""

    def new_ini(self, command):
        self.flush()
        self.i = self.last

    def bad_ini(self, command):
        self.flush()
        self.i = self.last

    def update_ini(self, command):
        self.i += self.last

    def new_mid(self, command):
        if self.f != "" or self.n != "":
            self.flush()
        if self.i == "":
            self.n = ""
            self.f = ""
            if self.f2 != "":
                self.i = self.f2
                self.f2 = ""
            else:
                self.i = self.f1
                self.f1 = ""
        self.m = self.last

    def bad_mid(self, command):
        self.flush()
        self.m = self.last
        self.flush()


    def update_mid(self, command):
        self.m += self.last

    def new_fin(self, command):
        self.f1 = self.last
        self.f2 = ""
        self.f = ""
        self.n = self.f1
        self.should_split_fin = False

    def complex_fin(self, command):
        if self.f1[-1] == self.last:
            self.f1 += self.last
            self.n = self.f1
        else:
            self.f2 += self.last
            self.f = self.f1
            self.n = self.f2
        self.should_split_fin = False

    def split_fin(self, command):
        if self.f1[-1] == self.last:
            self.f1 += self.last
            self.n = self.f1
        else:
            self.f2 += self.last
            self.f = self.f1
            self.n = self.f2
        self.should_split_fin = True

    def split_and_new_mid(self, command):
        if len(self.f2) > 0:
            tmp = self.f2
        else:
            tmp = self.f1
        self.flush()
        self.i = tmp
        self.m = self.last

    def bad_fin(self, command):
        if self.f2 != "":
            tmp = self.f2
        else:
            tmp = self.f1
        self.flush()
        self.i = tmp
        self.flush()
        self.i = self.last

    def abort(self, command):
        if not self.should_split_fin:
            self.f += self.n
            self.n = ""
        self.flush()

    def back(self):
        self.flush()
        self.i = ""
        if len(self.text) > 0:
            self.text = self.text[:-1]


# 초성
expr = "4+|5+|6+|7+|8+|9+|0+"
idfa = get_dfa(expr)

# 중성
expr  = "(122?|22?1|3|23|32|2312|3221)1?"
expr += "|1|223|322|2|22"
mdfa = get_dfa(expr)

# 종성
e4 = "(4(444)*)"; e5 = "(5(55)*)"; e6 = "(6(666)*)"
e44 = "(44(444)*)"; e55 = "(55)+"; e66 = "(66(666)*)"
e444 = "(444)+"; e666 = "(666)+"
e7 = "(7(777)*)"; e8 = "(8(888)*)"; e9 = "(9(999)*)"
e77 = "(77(777)*)"; e88 = "(88(888)*)"; e99 = "(99(999)*)"
e777 = "(777)+"; e888 = "(888)+"; e99 = "(999)+"
e0 = "(0(00)*)"; e00 = "(00)+"
expr  =  "(%s|%s)%s?"%(e4,e7,e8)      # [ㄱㅂ]ㅅ?
expr += "|(%s(%s|%s)?)"%(e5,e9,e88)   # ㄴ[ㅈㅎ]?
expr += "|(%s(%s|%s|%s|%s|%s|%s|%s)?)"%(e55,e4,e00,e7,e8,e66,e77,e88)   # ㄹ[ㄱㅁㅂㅅㅌㅍㅎ]?
expr += "|%s|%s|%s|%s|%s|%s"%(e6,e00,e8,e0,e9,e99)   # [ㄷㅁㅅㅇㅈㅊ]
expr += "|%s|%s|%s|%s|%s|%s"%(e44,e66,e77,e88,e444,e888)   # [ㅋㅌㅍㅎㄲㅆ]
fdfa = get_dfa(expr)

# Fallback for cases like ㄴㅅ->ㄶ->ㄴㅆ
expr = "(4+|5+|6+|7+|8+|9+|0+)(4+|5+|6+|7+|8+|9+|0+)"
f2dfa = get_dfa(expr)

class PhoneAutomata:
    def __init__(self, FinFirst=True, debug=False):
        self.debug = debug
        self.idfa = copy.deepcopy(idfa)
        self.mdfa = copy.deepcopy(mdfa)
        self.fdfa = copy.deepcopy(fdfa)
        self.f2dfa = copy.deepcopy(f2dfa)

        if FinFirst:
            self.writer = FinFirstWriter()
        else:
            self.writer = IniFirstWriter()
        self.mealy = get_mealy(self.writer)

        self.last_dfa = None

        self.state_history = [self.mealy.current]
        self.dfa_history = [self.idfa]

    def select_dfa(self, symbol):
        curr = self.mealy.current
        result = None
        if symbol in list("123"):
            if self.debug: print "m",
            result = self.mdfa
        else:
            if curr == "S" or curr == "I":
                if self.debug: print "i",
                result = self.idfa
            else:
                if self.debug: print "f",
                result = self.fdfa
        self.dfa_history.append(result)
        return result

    def feed(self, symbol):
        # Select proper DFA depending on input
        # and current superstate
        if self.debug: print symbol,
        dfa = self.select_dfa(symbol)

        # When current dfa is changed, reset
        # the previous one for future use.
        if not self.last_dfa:
            self.last_dfa = dfa
        if self.last_dfa and self.last_dfa != dfa:
            self.last_dfa.reset()
            if self.last_dfa == self.fdfa:
                self.f2dfa.reset()
            self.last_dfa = dfa
            if self.debug: print "RESET",
        else:
            if self.debug: print "     ",

        # Check if selected DFA accepts the input
        valid = dfa.feed(symbol)
        valid2 = None
        if dfa == self.fdfa:
            valid2 = self.f2dfa.feed(symbol)
        if self.debug: print self.mealy.current, valid, valid2,

        # Send control signals
        self.writer.set_last_symbol(symbol)
        if symbol in list("123"):
            if valid:
                self.mealy.feed("goodv")
            else:
                self.mealy.feed("badv")
        else:
            if valid:
                self.mealy.feed("goodc")
            elif valid2:
                self.mealy.feed("goodc2")
            else:
                self.mealy.feed("badc")
        self.state_history.append(self.mealy.current)
        if self.debug: print self.mealy.current,

    def next(self):
        if self.last_dfa:
            self.last_dfa.reset()
            if self.last_dfa == self.fdfa:
                self.f2dfa.reset()
        self.mealy.feed("next")

    def back(self):
        self.mealy.current = "S"
        self.writer.back()
        self.idfa.reset()
        self.mdfa.reset()
        self.fdfa.reset()
        self.f2dfa.reset()

