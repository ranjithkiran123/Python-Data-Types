set_a = set(input().split())
result = True

for _ in range(int(input())):
    tmp_set = set(input().split())
    if not set_a.issuperset(tmp_set):
        result = False
        break
    
print(result)
