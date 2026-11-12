from pda_cfg.validators import validate_arithmetic,validate_parentheses,validate_palindrome
def show(title,vals,fn):
 print('\n--- '+title+' ---')
 for x in vals: print(f"{x!r:22} -> {'ACCEPTED' if fn(x) else 'REJECTED'}")
def main():
 show('Arithmetic',['a','a+b','a*b','a+b*c','(a+b)*c','(a+b)*(c+d)','a+','+a','a**b','(a+b','a+b)','a(b+c)'],validate_arithmetic)
 show('Balanced Parentheses',['()','(())','()()','(()())','((()))','(',')','())(','(()','())'],validate_parentheses)
 show('Palindromes',['a','b','aa','aba','abba','aabbaa','ab','aabb','abab','abb','aaba','abc'],validate_palindrome)
if __name__=='__main__':main()
