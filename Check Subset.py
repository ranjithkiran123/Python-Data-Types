n = int(input())

for _ in range(n):
    a1 = int(input())
    s1 = set(map(int,input().split()))
    b1 = int(input())
    s2 = set(map(int, input().split()))
    
    print(s1.issubset(s2))
