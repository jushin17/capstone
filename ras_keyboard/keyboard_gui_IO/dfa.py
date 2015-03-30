#-*- coding: utf-8 -*-

def get_2d(d, x, y):
    try:
        return d[x][y]
    except (KeyError, ValueError):
        return None

def set_2d(d, x, y, z):
    tmp = d.get(x, {})
    tmp[y] = z
    d[x] = tmp
    return z

class DFA:

    def __init__(self, d):
        self.states = d["states"]
        self.symbols = d["symbols"]
        self.rules = d["rules"]
        self.initial = d["initial"]
        self.finals = d["finals"]
        self.current = self.initial
        self.history = [self.current]

    def transition(self, state, symbol):
        try:
            state = self.rules[state][symbol]
        except (KeyError, ValueError):
            return None
        return state

    def run(self, string):
        current = self.initial

        for symbol in string:
            current = self.transition(current, symbol)
            if current == None:
                return False

        if current in self.finals:
            return True
        else:
            return False

    def feed(self, symbol):
        self.history.append(self.current)
        self.current = self.transition(self.current, symbol)
        if self.current == None:
            return False    # Rejected.
        if self.current in self.finals:
            return True     # Accepted.
        return None         # Undecided yet.

    def reset(self):
        self.current = self.initial
        self.history = []

    def back(self):
        if len(self.history) > 0:
            self.current = self.history.pop()

    def mark_reachable(self, visited, p):
        """
        Remove unreachable states.
        """
        if visited.get(p, False):
            return
        visited[p] = True
        for a in self.rules.get(p, {}):
            q = self.rules[p][a]
            self.mark_reachable(visited, q)

    def dump_table(self, table):
        num_states = len(self.states)
        prt = {None:"-", True:"1", False:"0"}
        for i in range(num_states):
            p = self.states[i]
            print p, "|",
            for j in range(i):
                q = self.states[j]
                print prt[get_2d(table, p, q)],
            print
        print "--|",
        for i in range(num_states):
            print self.states[i],
        print
        print

    def get_new_state(self):
        """Allocates new state"""
        new = len(self.states)
        while new in self.states:
            new += 1
        return new

    def merge_states(self, M):
        """
        Merge states in the set M.
        """
        # Allocate new, merged state.
        new = self.get_new_state()
        self.states.append(new)

        # If M is set of final states,
        # Modify the final state.
        if M[0] in self.finals:
            for p in M:
                if p in self.finals:
                    self.finals.remove(p)
            self.finals.append(new)

        # if M contains an initial state,
        # then the new state becomes the initial state.
        for p in M:
            if p == self.initial:
                self.initial = new

        # Redirect arrows pointing to one of M
        # to point the new state.
        # If p,a => M, Then p,a => new.
        for p in self.states:
            for a in self.symbols:
                if self.transition(p, a) in M:
                    set_2d(self.rules, p, a, new)

        # Move arrows starting from one of M
        # to start from the new state.
        # If M,a => q, then new,a => q
        for p in M:
            for a in self.symbols:
                q = get_2d(self.rules, p, a)
                if q:
                    set_2d(self.rules, new, a, q)

        # Remove original states.
        for p in M:
            if p in self.states:
                self.states.remove(p)
            if p in self.rules:
                del self.rules[p]

    def collect_group(self, table, group, visited, p):
        """
        Perform depth-first search to collect group of states
        that are indistinguishable each other.
        """
        if visited.get(p, False):
            return

        group.append(p)
        visited[p] = True

        for q in table.get(p, {}):
            if table[p][q] == False:
                self.collect_group(table, group, visited, q)

    def minimize(self):
        # Remove unreacheable states
        visited = {}
        self.mark_reachable(visited, self.initial)
        for p in self.states:
            if not visited.get(p, False):
                self.states.remove(p)
                if p in self.rules:
                    del self.rules[p]

        # Run table-filling algorithm to find pairs of
        # indistinguishable states.
        unknown = []
        table = {}
        num_states = len(self.states)
        for i in range(num_states):
            for j in range(i):
                set_2d(table, i, j, False)

        # A final state and non-final state is distinguishable.
        for i in range(num_states):
            for j in range(i):
                p = self.states[i]
                q = self.states[j]
                if   p in self.finals and q not in self.finals:
                    set_2d(table, i, j, True)
                elif q in self.finals and p not in self.finals:
                    set_2d(table, i, j, True)

        for i in range(num_states):
            for j in range(i):
                if get_2d(table, i, j) == False:
                    unknown.append((i,j))

        # Recursive step of the algorithm
        while len(unknown) > 0:
            i, j = unknown.pop()
            p = self.states[i]
            q = self.states[j]

            for a in self.symbols:
                pp = self.transition(p, a)
                qq = self.transition(q, a)
                ii = self.states.index(pp)
                jj = self.states.index(qq)
                if get_2d(table, ii, jj) == True:
                    set_2d(table, i, j, True)
                    break

        # Build minimized DFA based on the table-filling result.
        visited = {}
        orig_states = self.states
        groups = []
        for p in self.states:
            if not visited.get(p, False):
                group = []
                self.collect_group(table, group, visited, p)
                if len(group) > 1:
                    groups.append(group)

        for group in groups:
            self.merge_states(group)

        return self

    def dump(self):
        print "states:", self.states
        print "symbols:", self.symbols
        print "rules:", self.rules
        print "initial:", self.initial
        print "finals:", self.finals

