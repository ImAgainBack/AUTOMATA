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

#-------------------------------------PRINTS TABLE AUTOMATA------------------------------------------

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
        
#-------------------------------------PRINTS TABLE AUTOMATA------------------------------------------

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

    
#------------------------------RETURNS COMPLETE AUTOMATA-------------------------------------------
def make_complete_array1(array_first_line,array_second_line,array_fith_line, array_data_6th_line):
    nrows: int = len(array)      #works for deterministic non-complete automaton only
    i : int=0
    alphabet_size: int =array_first_line
    number_of_states=array_second_line
    for j in range(0,nrows):
        while(array_data_6th_line[2][j]!="p"): #the function will stop compiling when it reaches a row containing the p state, meaning the automaton is already complete
            if alphabet_size==1:  #in the case the only letter recognized is "a" for example
                if array_data_6th_line[0][j]==i: #it will detect which lines are missing to make the automaton complete
                    i+=1
                    j+=1
                else:
                    new_row=["i","a","p"]     #create a row that will be inserted to complete
                    array_data_6th_line=array_data_6th_line.append(new_row, ignore_index=True)
                    array_fifht_line+=1      #because we added 1 transition
                    i+=1
            #the function is not able to deal with 2 letters alphabet yet
    if alphabet_size==1:
        sink_row=["p", "a", "p"]
        array_data_6th_line = array_data_6th_line.append(sink_row, ignore_index=True) #we add the sink row at the end
    return array_data_6th_line
#------------------------------RETURNS COMPLETE AUTOMATA-------------------------------------------

#-----------------------------GRAPHICAL REPRESENTATION------------------------------------
def display_finite_automaton(file_name):
    # open the file and read the data
    with open(file_name, 'r') as f:
        number_of_symbols = int(f.readline())
        number_of_states = int(f.readline())
        nb_of_initial_states = list(map(int, f.readline().split()))
        nb_of_final_states = list(map(int, f.readline().split()))
        nb_of_transitions = int(f.readline())
        transitions = [f.readline().split() for _ in range(nb_of_transitions)]

    # create a dictionary of transitions
    transition_dict = {}
    for transition in transitions:
        state_from = int(transition[0])
        state_to = int(transition[2])
        label = transition[1]
        # check if the state has already been added to the dictionary
        if state_from not in transition_dict:
            transition_dict[state_from] = []
        # add the transition to the dictionary
        transition_dict[state_from].append((state_to, label))

    # create the Graphviz object
    dot = graphviz.Digraph()

    # add the states to the Graphviz object
    for i in range(number_of_states):
        # check if the state is an initial state
        if i in nb_of_initial_states:
            # add the start node for each initial state
            for index, initial_state in enumerate(nb_of_initial_states):
                if i == initial_state:
                    dot.node(f'start{index}', shape='point')
                    dot.edge(f'start{index}', str(i), label='', arrowhead='normal')
            # add the circle node for each state that is not an initial state
            dot.node(str(i), shape='circle')
        # check if the state is a final state
        elif i in nb_of_final_states:
            dot.node(str(i), shape='doublecircle')
        else:
            # add the circle node for each state that is not an initial state or a final state
            dot.node(str(i), shape='circle')

    # add the transitions to the Graphviz object
    for state_from, transitions in transition_dict.items():
        # group the transitions that go from the same state to the same state
        for state_to, labels in groupby(sorted(transitions), key=lambda x: x[0]):
            # combine the labels for the grouped transitions
            label = ','.join([x[1] for x in labels])
            # add the edge to the Graphviz object
            dot.edge(str(state_from), str(state_to), label=label)

    # render and view the Graphviz object
    dot.render('automate', format='png', view=True)


def is_automaton_complete(file_name):
    # open the file and read the data
    with open(file_name, 'r') as f:
        number_of_symbols = int(f.readline())
        number_of_states = int(f.readline())
        nb_of_initial_states = list(map(int, f.readline().split()))
        nb_of_final_states = list(map(int, f.readline().split()))
        nb_of_transitions = int(f.readline())
        transitions = [f.readline().split() for _ in range(nb_of_transitions)]

    # create a dictionary of transitions
    transition_dict = {}
    for transition in transitions:
        state_from = int(transition[0])
        state_to = int(transition[2])
        label = transition[1]
        if state_from not in transition_dict:
            transition_dict[state_from] = []
        transition_dict[state_from].append((state_to, label))

    # verify if the automaton is complete
    for state in range(number_of_states):
        if state not in transition_dict:
            return False
        labels = set([x[1] for x in transition_dict[state]])
        if len(labels) != number_of_symbols:
            return False

    return True


# call the function with the filename of the automaton
print("The automaton is complete : ", is_automaton_complete('automate.txt'))
display_finite_automaton('automate.txt')

#-----------------------------GRAPHICAL REPRESENTATION------------------------------------
