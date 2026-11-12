def balanced_parentheses_pda_trace(text):
    """PDA: push '(' and pop on ')'. Accept iff stack is empty at end."""
    stack=[]; trace=[("q0","start","Z")]
    for ch in text:
        if ch=='(': stack.append('(')
        elif ch==')':
            if not stack: return False,trace
            stack.pop()
        else: return False,trace
        trace.append(("q0",ch,"Z"+''.join(stack)))
    return not stack,trace

def palindrome_pda_trace(text):
    """Conceptual nondeterministic PDA trace: push first half, guess middle, pop second half."""
    if any(c not in 'ab' for c in text): return False,[]
    n=len(text); half=n//2; first=text[:half]; second=text[half+(n%2):]
    ok=first==second[::-1]
    return ok,[('push',first,''.join(first) or 'epsilon'),('middle',text[half:half+(n%2)] or 'epsilon',''),('pop',second,'epsilon' if ok else 'mismatch')]
