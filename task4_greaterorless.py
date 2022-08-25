def math(o, p, k):
    if o > p:
        print("Couldn't be better!")
    elif o == p:
        if k > p:
            print("Nice!")
        else: print("It could be worse!")
    elif o < p:
        print("Couldn't be helped!")


o = int(input())
p = int(input())
k = int(input())
math(o, p, k)