from .validators import *
def main():
    while True:
        print("\n1 Arithmetic  2 Parentheses  3 Palindrome  4 Exit")
        c=input("Choose: ").strip()
        if c=='1': print('ACCEPTED' if validate_arithmetic(input('Expression: ')) else 'REJECTED')
        elif c=='2':
            s=input('Parentheses: '); ok,tr=parentheses_trace(s); print('ACCEPTED' if ok else 'REJECTED'); print(*tr,sep='\n')
        elif c=='3':
            s=input('Palindrome over a,b: '); ok,tr=palindrome_trace(s); print('ACCEPTED' if ok else 'REJECTED'); print(*tr,sep='\n')
        elif c=='4': break
        else: print('Invalid option')
if __name__=='__main__':main()
