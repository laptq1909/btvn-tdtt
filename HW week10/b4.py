for _ in range(int(input())):
    s1 = input()
    s2 = input()

    idx = 0
    ok = 0
    for i in range(len(s1)):
        c1 = s1[i].lower()
        c2 = s2[idx].lower()
        if c1 == c2:
            idx += 1
        if idx == len(s2):
            ok = 1
            break
    if ok: print("YES")
    else: print("NO")