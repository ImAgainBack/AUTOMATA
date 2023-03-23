def lines(line): #a function that gents 1 line and splits values in a list
    data = line.split()
    return data

def remaining_lines(line): #function that gets used in the 6th line and so on
    data = line.split()
    data_6th_line.append(data) #for that we create a 2d array
    return data

data_6th_line=[] #creation of the 2d array
with open('text_file.txt') as file: #opening the txt file containing automata
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


def standart(): #checking if the automata is standart
    state=True #bool value check
    if len(third_line)==1: #cheking if there is multiple initial states, if so will go to line 38 and print False, meaning not standart
        initial_state=third_line[0] #collecting the int value of the 4rd line, which is the initial state

        for i in range(len(data_6th_line)): #loop to lopp through all the elements in the 2d array
    
            if initial_state==data_6th_line[i][2]:#loop to check if there is a match between the 3rd element of the 2d array 

                state=False #if there is a match between the last element of the 2d array and the initial state, not standart automata
    else:
        return False 
    return state
