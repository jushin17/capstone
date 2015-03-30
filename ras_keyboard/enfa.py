from dfa import DFA
import random

def add_set(a, b):
    return list(set(a + b))

def add_2d_dict(d, x, y, z):
    """
    Robustly set d[x][y] = z
    """
    tmp = d.get(x, {})
    tmp[y] = z
    d[x] = tmp

def get_2d(d, x, y):
    try:
        return set(d[x][y])
    except (KeyError, ValueError):
        return set()

class ENFA:
    def __init__(self, d):
        self.states = set(d["states"])
        self.symbols = set(d["symbols"])
        self.rules = d["rules"]
        self.initial = d["initial"]
        self.finals = set(d["finals"])

    def try_get(self, state, symbol):
        try:
            return set(self.rules[state][symbol])
        except (KeyError, ValueError):
            return set()

    def e_move(self, states):
        """
        epsilon move from set of states to set of states.
        """
        move = set()
        for p in states:
            move |= set(self.try_get(p, ""))
        return move

    def e_closure(self, state):
        """
        Set of states reachable from the given state
        using only epsilon moves.
        """
        closure = set([state])
        while True:
            new_closure = closure | self.e_move(closure)
            if new_closure == closure:
                break
            closure = new_closure
        return closure

    def transition(self, states, symbol):
        """
        State transition from a set of states to another set of states
        with given symbol.
        """
        dest = set()
        for p in states:
            dest |= self.try_get(p, symbol)
        edest = dest.copy()
        for p in dest:
            edest |= self.e_closure(p)
        return edest

    def run(self, string):
        current = self.e_closure(self.initial)
        for symbol in string:
            current = self.transition(current, symbol)
            if current == set():
                return False

        if self.finals & current != set():
            return True
        else:
            return False

def random_id():
    """
    Generates a random 16bit number.
    Used as a state name to avoid collision.
    """
    return hex(int(random.getrandbits(32)))[2:]

class ENFABuilder:

    @staticmethod
    def empty():
        """
        Returns an e-NFA that accepts empty string.
        """
        i = random_id()
        d = {
            "states": [i],
            "symbols": [],
            "rules": {},
            "initial": i,
            "finals": [i],
        }
        return ENFA(d)

    @staticmethod
    def simple(symbol):
        """
        Returns an e-NFA that accepts only the given symbol.
        This is the bottommost building block of the e-NFA for RE.
        """
        i = random_id();
        f = random_id();
        d = {
            "states": [i, f],
            "symbols": [symbol],
            "rules": { i: {symbol: [f]} },
            "initial": i,
            "finals": [f],
        }
        return ENFA(d)

    @staticmethod
    def chars(symbols):
        """
        Returns and e-NFA that accepts one of the given symbol.
        """
        i = random_id()
        f = random_id()
        rule = {}
        rule[i] = {}
        for symbol in symbols:
            rule[i][symbol] = set([f])

        d = {\
            "states": [i, f],
            "symbols": symbols,
            "rules": rule,
            "initial": i,
            "finals": [f],
        }
        return ENFA(d)

    @staticmethod
    def rename(A):
        """Rename the states of e-NFA A to some random names."""
        conv = {}
        for state in A.states:
            conv[state] = random_id();

        new_rule = {}
        for p in A.states:
            new_p = conv[p]
            for a in A.symbols | set(['']):
                q = A.try_get(p,a)
                if q != set():
                    new_q = map(conv.get, q)
                    add_2d_dict(new_rule, new_p, a, new_q)

        d = {
            "states": map(conv.get, A.states),
            "symbols": A.symbols,
            "rules": new_rule,
            "initial": conv[A.initial],
            "finals": map(conv.get, A.finals),
        }
        return ENFA(d)

    @staticmethod
    def concat(A, B):
        """
        Returns concatenated e-NFA of A and B. epsilon transitions from
        finals states of A to initial state of B are added.
        """
        A = ENFABuilder.rename(A)
        B = ENFABuilder.rename(B)

        new_rule = A.rules.copy()
        for p in B.states:
            for a in B.symbols | set(['']):
                tmp = B.try_get(p, a)
                if tmp != set():
                    add_2d_dict(new_rule, p, a, tmp)

        for f in A.finals:
            tmp = A.try_get(f, '')
            add_2d_dict(new_rule, f, '', tmp | set([B.initial]))

        d = {
            "states": A.states | B.states,
            "symbols": A.symbols | B.symbols,
            "rules": new_rule,
            "initial": A.initial,
            "finals": B.finals,
        }
        return ENFA(d)

    @staticmethod
    def repeat(A):
        """
        Returns new e-NFA that represents zero or more repetition of
        the language represented by A.
        """
        new_i = random_id()
        new_f = random_id()

        new_rule = A.rules.copy()
        new_rule[new_i] = {'': set([A.initial, new_f])}

        for f in A.finals:
            tmp = A.try_get(f, '')
            add_2d_dict(new_rule, f, '', tmp | set([A.initial, new_f]))

        d = {
            "states": A.states | set([new_i, new_f]),
            "symbols": A.symbols,
            "rules": new_rule,
            "initial": new_i,
            "finals": set([new_f]),
        }
        return ENFA(d)

    @staticmethod
    def union(A, B):
        """
        Returns new e-nFA that represents the language of strings
        accepted by A or B.
        """
        A = ENFABuilder.rename(A)
        B = ENFABuilder.rename(B)

        new_i = random_id()
        new_f = random_id()

        new_rule = A.rules.copy()
        for p in B.states:
            for a in B.symbols | set(['']):
                tmp = B.try_get(p, a)
                if tmp != set():
                    add_2d_dict(new_rule, p, a, tmp)

        add_2d_dict(new_rule, new_i, '', set([A.initial,B.initial]))

        for f in A.finals:
            tmp = A.try_get(f, '')
            add_2d_dict(new_rule, f, '', tmp | set([new_f]))

        for f in B.finals:
            tmp = B.try_get(f, '')
            add_2d_dict(new_rule, f, '', tmp | set([new_f]))

        d = {
            "states": A.states | B.states | set([new_i, new_f]),
            "symbols": A.symbols | B.symbols,
            "rules": new_rule,
            "initial": new_i,
            "finals": set([new_f]),
        }
        return ENFA(d)


class ENFAToDFAConverter:
    """
    Converts an ENFA into a DFA
    """
    def __init__(self, enfa):
        self.enfa = enfa

        # A list of set of states.
        # Effectively a mapping (DFA state) -> (eNFA states)
        self.d_states = []

        # DFA transition function
        # (DFA state) x (symbol) -> (DFA state)
        self.d_rules = {}

        # List of states in which transition rules
        # from that state is not completely known.
        # The conversion ends when this list becomes empty.
        self.todo_states = []

    def get_or_push_state(self, enfa_states):
        """
        Given set of ENFA states,
        if it has assigned a DFA state, return the corresponding DFA state.
        Otherwise, push the given set to the state mapping (d_states) and
        return the corresponding DFA state number.
        """
        for i in range(len(self.d_states)):
            if self.d_states[i] == enfa_states:
                return i
        self.d_states.append(enfa_states)
        i = len(self.d_states) - 1
        self.todo_states.append(i)
        return i

    def add_rule(self, dfa_src, symbol):
        """
        Find and save a transition rule from the given DFA state, with given
        symbol. This is computed based on the ENFA rules.
        """
        enfa_src = self.d_states[dfa_src]
        enfa_dst = self.enfa.transition(enfa_src, symbol)
        dfa_dst = self.get_or_push_state(enfa_dst)
        add_2d_dict(self.d_rules, dfa_src, symbol, dfa_dst)

    def convert(self):
        """The main conversion routine."""
        i = self.enfa.e_closure(self.enfa.initial)
        dfa_initial = self.get_or_push_state(i)

        while len(self.todo_states) > 0:
            dfa_src = self.todo_states.pop()
            for symbol in self.enfa.symbols:
                self.add_rule(dfa_src, symbol)

        dfa_finals = []
        for i in range(len(self.d_states)):
            if self.d_states[i] & self.enfa.finals != set():
                dfa_finals.append(i)

        d = {
            "states": range(len(self.d_states)),
            "symbols": self.enfa.symbols,
            "rules": self.d_rules,
            "initial": dfa_initial,
            "finals": dfa_finals,
        }
        return DFA(d)

