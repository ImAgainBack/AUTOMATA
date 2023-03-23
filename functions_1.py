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
