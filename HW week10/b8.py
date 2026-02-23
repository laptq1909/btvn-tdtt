def is_path_crossing(moves):
    se = set()
    se.add((0, 0))
    x = 0
    y = 0
    for i in moves:
        if i == "R":
            y += 1
            if (x, y) in se:
                return True
        elif i == "L":
            y -= 1
            if (x, y) in se:
                return True
        elif i == "U":
            x -= 1
            if (x, y) in se:
                return True
        elif i == "D":
            x += 1
            if (x, y) in se:
                return True
        se.add((x, y))
    return False

moves = input()
print(is_path_crossing(moves))