n=int(input())

set1=set(input().split())

for i in range(int(input())):

    ope,cou=input().split()

    getattr(set1,ope)(input().split())
    se=list(map(int,set1))

print(sum(se))
