import graphviz
from itertools import groupby


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



def display_finite_automaton(file_name):
    # open the file and read the data
    with open(file_name, 'r') as f:
        number_of_symbols = int(f.readline())
        number_of_states = int(f.readline())
        initial_states = list(map(int, f.readline().split()))
        final_states = list(map(int, f.readline().split()))
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
        if i in initial_states:
            # add the start node for each initial state
            for index, initial_state in enumerate(initial_states):
                if i == initial_state:
                    dot.node(f'start{index}', shape='point')
                    dot.edge(f'start{index}', str(i), label='', arrowhead='normal')
            # add the circle node for each state that is not an initial state
            dot.node(str(i), shape='circle')
        # check if the state is a final state
        if i in final_states:
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