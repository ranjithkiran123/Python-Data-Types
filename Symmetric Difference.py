M = int(input())
a = set(map(int, input().split()))
N = int(input())
b = set(map(int,input().split()))

sym = sorted(x for x in a.symmetric_difference(b))
for elems in sym:
    print(elems)
