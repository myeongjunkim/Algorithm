

# data = [line, line, line]

line = "+-----+-+\n"
line = "| +------ "
line = "| -- -------"


real_data=[]

i = 0
for line in data:
    
    data_line = []
    for j in range(len(data[i])):
        
        if data[i][j+1] == "-":
            if data[i+1][j] == "|":
                # 오른쪽 -, 아래 |
                data_line.append(3)
            else:
                # 오른쪽 -, 아래 x
                data_line.append(1)

        else        
            if data[i+1][j] == "|":
                # 오른쪽x, 아래 O
                data_line.append(2)
            else:
                data_line.append(0)

        j += 2


    i +=2

    real_data.append(data_line)



