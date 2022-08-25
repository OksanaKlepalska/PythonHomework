def math(l, m, n):
    if l >= m:
        print("Fabulous!")
    while l < m:
        print(l)
        l += n
        if l >= m:
            print (l)
            break


l = int(input())
m = int(input())
n = int(input())
math(l, m, n)