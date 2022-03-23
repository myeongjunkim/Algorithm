def make_map(data):

    data = data[1:]
    data.append(" "*19)

    real_data=[]
    for i in range(0, len(data), 2):
        
        data_line = []
        for j in range(0, len(data[i]), 2):
            
            if data[i][j+1] == "-":
                if data[i+1][j] == "|":
                    # 오른쪽 -, 아래 |
                    data_line.append(3)
                else:
                    # 오른쪽 -, 아래 x
                    data_line.append(1)
            else:
                if data[i+1][j] == "|":
                    # 오른쪽x, 아래 O
                    data_line.append(2)
                else:
                    data_line.append(0)

        real_data.append(data_line)


    return real_data


# main
data = []
with open("maze1.txt") as f:
    while True:
        line = f.readline()
        if not line: break
        data.append(line)

real_data = make_map(data)



for line in real_data:
    next_line = ""
    for c in line:
        if c == 3:
            print("+-", end="")
            next_line += "| "
        elif c == 2:
            print("| ", end="")
            next_line += "| "
        elif c == 1:
            print("--", end="")
            next_line += "  "
        elif c == 0:
            print("  ", end="")
            next_line += "  "
    print("")
    print(next_line)



sum = 0
for line in real_data:
    sum += len(line)