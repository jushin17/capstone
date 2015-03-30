from ply import lex
from ply import yacc

from enfa import ENFABuilder

#----------------------------------
# LEX Definitions
#----------------------------------

class RegexLexer:
    tokens = (
        "ALPHA", "DOT",
        "STAR", "BAR", "PLUS", "QUESTION",
        "LPAREN", "RPAREN",
        "BACKSLASH",
    )

    t_DOT = r"\."
    t_STAR = r"\*"
    t_BAR = r"\|"
    t_PLUS = r"\+"
    t_QUESTION = r"\?"
    t_LPAREN = r"\("
    t_RPAREN = r"\)"
    t_BACKSLASH = r"\\"

    def t_ALPHA(self, t):
        r"[0-9a-zA-Z:/@]"
        return t;

    def t_error(self, t):
        print "Error at '%s'" % t.value[0]
        t.lexer.skip(1)

    def __init__(self):
        self.lexer = lex.lex(module=self)

#----------------------------------
# YACC Definitions
#----------------------------------

class RegexParser:

    precedence = (
        ('left', 'BAR'),
        ('left', 'DOT', 'ALPHA'),
        ('left', 'CONCAT'),
        ('right', 'STAR', 'PLUS', 'QUESTION'),
        ('left', 'BACKSLASH'),
    )

    def p_regex_expr(self, p):
        "regex : expr"
        p[0] = p[1]
        p[0].s = p[1].s

    def p_regex_empty(self, p):
        "regex : "
        p[0] = ENFABuilder.empty()
        p[0].s = ''

    def p_escape(self, p):
        """
        expr : BACKSLASH DOT
             | BACKSLASH STAR
             | BACKSLASH PLUS
             | BACKSLASH QUESTION
             | BACKSLASH BAR
             | BACKSLASH LPAREN
             | BACKSLASH RPAREN
             | BACKSLASH BACKSLASH
        """
        p[0] = ENFABuilder.simple(p[2])
        p[0].s = '\\'+p[2]

    def p_expr_group(self, p):
        "expr : LPAREN expr RPAREN"
        p[0] = p[2]
        p[0].s = p[2].s

    def p_expr_star(self, p):
        "expr : expr STAR"
        p[0] = ENFABuilder.repeat(p[1])
        p[0].s = ('*', p[1].s)

    def p_expr_plus(self, p):
        "expr : expr PLUS"
        star = ENFABuilder.repeat(p[1])
        p[0] = ENFABuilder.concat(p[1], star)
        p[0].s = ('+', p[1].s)

    def p_expr_question(self, p):
        "expr : expr QUESTION"
        empty = ENFABuilder.empty()
        p[0] = ENFABuilder.union(empty, p[1])
        p[0].s = ('?', p[1].s)

    def p_expr_chain(self, p):
        "expr : expr expr %prec CONCAT"
        p[0] = ENFABuilder.concat(p[1], p[2])
        p[0].s = ('&', p[1].s, p[2].s)

    def p_expr_dot(self, p):
        "expr : DOT"
        all_chars  = range(ord('0'), ord('9')+1)
        all_chars += range(ord('a'), ord('z')+1)
        all_chars += range(ord('A'), ord('Z')+1)
        all_chars = map(chr, all_chars)
        p[0] = ENFABuilder.chars(all_chars)
        p[0].s = '.'

    def p_expr_alpha(self, p):
        "expr : ALPHA"
        p[0] = ENFABuilder.simple(p[1])
        p[0].s = p[1]

    def p_expr_bar(self, p):
        "expr : expr BAR expr"
        p[0] = ENFABuilder.union(p[1], p[3])
        p[0].s = ('|', p[1].s, p[3].s)

    def p_error(self, p):
        print "Not grammatical '%s'" % p.value

    def __init__(self):
        self.lexer = RegexLexer()
        self.tokens = self.lexer.tokens
        self.parser = yacc.yacc(module=self)

    def parse(self, data):
        return self.parser.parse(data, self.lexer.lexer)

