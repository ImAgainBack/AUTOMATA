#-------------------------------------ALLOWS TO READ FILE-----------------------------
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
#-------------------------------------ALLOWS TO READ FILE-----------------------------

def standart(): #checking if the automata is standart
    state=True #bool value check
    if len(third_line)==1: #cheking if there is multiple initial states, if so will go to line 38 and print False, meaning not standart
        initial_state=third_line[0] #collecting the int value of the 3rd line, which is the initial state

        for i in range(len(data_6th_line)): #loop to lopp through all the elements in the 2d array
    
            if initial_state==data_6th_line[i][2]:#loop to check if there is a match between the 3rd element of the 2d array 

                state=False #if there is a match between the last element of the 2d array and the initial state, not standart automata
    else:
        return False 
    return state

def print_automata_array():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    result = ''
    file = open('text_file.txt', 'r')
    read = file.readlines()
    for i in range(int(read[0])):
        result += alphabet[i] + "  "
    print("     | " + result)
    print("-----+" + int(read[0]) * '---')             #so far we print the alphabet with the right format
    for j in range(int(read[1])):       #first "for" loop with j going through every state
        for k in range(int(read[0])):        #for transitions k goes through the hole alphabet of the automata
            current_letter=''
            for i in range(int(read[4])):           #for every transitions one compare the state and the transition
                if j == int(read[i+5][0]):
                    if read[i+5][2] == alphabet[k]:
                        current_letter += read[i+5][4] + ','
            if current_letter == '':
                current_letter = '-'
            else:
                current_letter = current_letter[0:len(current_letter)-1]
            if k == 0:
                bool = False
                for p in range(2 * int(read[2][0])):
                    if str(j) == read[2][p]:
                        print('-> ' + str(j) + " | " + current_letter, end="")
                        bool = True
                for l in range(2 * int(read[3][0])):
                    if str(j) == read[3][l]:
                        print('<- ' + str(j) + " | " + current_letter, end="")
                        bool = True
                if bool is False:
                    print('   ' + str(j) + " | " + current_letter, end="")
            else:
                print('  ' + current_letter, end="")
        print("\n")
        
        
def determinized(): #function to check if the automata is determinized 
    def find_duplicates(lst, indices): #by so we will find duplicates in the 2d array, check comments in functions_1
        seen = set()
        duplicates = set()
        for i, sublist in enumerate(lst):
            key = tuple(sublist[i] for i in indices)
            if key in seen:
                duplicates.add(i)
            seen.add(key)
        return duplicates

    duplicates = find_duplicates(data_6th_line, [0,1]) #[0,1] are elements in the 2d array, so we will check in the loop below if there is a match
        
    if duplicates==set(): #if no duplicates
        return True #this automata is determinized
    else:
        return False
