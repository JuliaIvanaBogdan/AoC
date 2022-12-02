def day1():
    f = open("input\day1.txt", "r")
    cals = []
    c = 0
    for line in f:
        if (line == "\n"):
            cals.append(c)
            c=0
        else:
            c = c+int(line)
    cals.sort(reverse=True)
    print("Part 1: " + str(max(cals)))
    print("Part 2: " + str(cals[0]+cals[1]+cals[2]))
    return

day1()

