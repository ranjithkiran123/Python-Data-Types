if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        cmd, *values = input().split()
        values = tuple(map(int, values))
        if cmd == "print":
            s = f"{cmd}(lst)"
        else:
            s = f"lst.{cmd}{values}"
        eval(s)
