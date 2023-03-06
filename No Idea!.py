input()
arr = map(int, input().split())

c = set(map(int, input().split()))
d = set(map(int, input().split()))

print(sum(1 if x in c else -1 if x in d else 0 for x in arr))
