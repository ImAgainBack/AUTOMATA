def lines(line):
    data = line.split()
    return data

def remaining_lines(line):
    data = line.split()
    data_6th_line.append(data)
    return data

data_6th_line=[]
with open('text_file.txt') as file:
    for i, line in enumerate(file):
        if i == 0:
            first_line=lines(line)
        elif i == 1:
            second_line=lines(line)
        elif i == 2:
            third_line=lines(line)
        elif i == 3:
            fourth_line=lines(line)
        elif i == 4:
            fifth_line=lines(line)
        else:
            remaining_lines(line)


def standart():
    state=True
    print(third_line)
    if len(third_line)==1:
        initial_state=third_line[0]

        for i in range(len(data_6th_line)):
    
            if initial_state==data_6th_line[i][2]:

                state=False
    else:
        return False
    return state
