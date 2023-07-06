def factor(n):
    if n == 0:
        return 1
    return factor(n-1) * n

n=int(input())
m=int(input())
print(factor(n+m-1)/(factor(m)*factor(n-1)))
