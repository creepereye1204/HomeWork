infix=list(input())
stack=[]
while infix:
    n=infix.pop(0)
    if ord('0')<=ord(n)<=ord('9'):
        print(n,end='')
    elif n=='(':
        stack.append(n)
    elif  n=='*' or n=='/':
        while stack and (stack[-1]=='*' or stack[-1]=='/'):
            print(stack.pop(),end='')
        stack.append(n)
    elif n=='+' or n=='-':
        while stack and stack[-1]!='(':
            print(stack.pop(),end='')
        stack.append(n)
    else:
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()
stack=stack[::-1]
print(''.join(stack) if stack else '',end='')
