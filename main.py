with open("matching.txt") as file:
    for line in file:
        i=0
        for char in line:
            i += 1
        print(i)