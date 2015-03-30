#-*- coding: utf-8 -*-

# mealy.py
# Mealy machine implementation in python
# 20130598 정윤종 <yunjong@kaist.ac.kr>

class Mealy:

    def __init__(self, definition):
        """
        The constructor for Mealy machine.
        Mealy machine is really just a DFA with output.

        states  = list of states, composed of objects that is not None.

        symbols = list of alphabets.

        rules   = a transition table, of type dictionary of dictionaries.
                  rules[p][x] = q
                      iff state p can transite to state q on input x.
                  Make d[p][x] to be undefined, or to return None
                      in order to indicate such transition is impossible.

        actions = A function table, of type dictionary of dictionaries.
                  if actions[p][x] = f,
                  then executes f(x)

        initial = The initial state. Must be an element of Q.
        """
        self.states = definition["states"]
        self.symbols = definition["symbols"]
        self.rules = definition["rules"]
        self.actions = definition["actions"]
        self.initial = definition["initial"]

        self.current = self.initial

    def feed(self, symbol):
        p = self.current
        x = symbol
        if x not in self.symbols:
            raise ValueError("unknown symbol")
        try:
            q = self.rules[p][x]
            f = self.actions[p][x]
            f(x)
            self.current = q
        except (KeyError, ValueError):
            print "Error transition from %s, %s" % (p, x)

