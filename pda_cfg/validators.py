import re
from .pda import balanced_parentheses_pda_trace,palindrome_pda_trace
TOKEN=re.compile(r"\s*(?:(?P<ID>[A-Za-z_][A-Za-z0-9_]*)|(?P<PLUS>\+)|(?P<MUL>\*)|(?P<LP>\()|(?P<RP>\)))")
class Parser:
    def __init__(self,s): self.t=[]; p=0
    def parse(self,s):
        self.t=[]; p=0
        while p<len(s):
            m=TOKEN.match(s,p)
            if not m: raise ValueError()
            self.t.append(m.lastgroup); p=m.end()
        if not self.t:return False
        self.p=0; self.E(); return self.p==len(self.t)
    def cur(self): return self.t[self.p] if self.p<len(self.t) else None
    def eat(self,x):
        if self.cur()!=x: raise ValueError()
        self.p+=1
    def E(self):
        self.T()
        while self.cur()=='PLUS': self.eat('PLUS'); self.T()
    def T(self):
        self.F()
        while self.cur()=='MUL': self.eat('MUL'); self.F()
    def F(self):
        if self.cur()=='ID': self.eat('ID')
        elif self.cur()=='LP': self.eat('LP'); self.E(); self.eat('RP')
        else: raise ValueError()
P=Parser()
def validate_arithmetic(s):
    try:return P.parse(s)
    except Exception:return False
def validate_parentheses(s):return balanced_parentheses_pda_trace(s)[0]
def validate_palindrome(s):return palindrome_pda_trace(s)[0]
def parentheses_trace(s):return balanced_parentheses_pda_trace(s)
def palindrome_trace(s):return palindrome_pda_trace(s)
