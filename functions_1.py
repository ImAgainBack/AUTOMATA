#-------------------------------------ALLOWS TO READ FILE-----------------------------
from itertools import groupby
import graphviz


def lines(line): #a function that gents 1 line and splits values in a list
    data = line.split()
    return data

def remaining_lines(line): #function that gets used in the 6th line and so on
    data = line.split()
    data_6th_line.append(data) #for that we create a 2d array
    return data

data_6th_line=[] #creation of the 2d array
def file_read(txt_file):
    with open(txt_file) as file: #opening the txt file containing automata
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
        return first_line, second_line, third_line,fourth_line, fifth_line, data_6th_line #for each line, one array dedicated
    #that can be called by file_read(txt_file)[] inside bracets you put your wished line

def read_automaton(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

        num_symbols = int(lines[0].strip())
        num_states = int(lines[1].strip())
        initial_states = list(map(int, lines[2].strip().split()))
        final_states = list(map(int, lines[3].strip().split()))
        num_transitions = int(lines[4].strip())
        transitions = [tuple(line.strip().split()) for line in lines[5:]]

        return num_symbols, num_states, initial_states, final_states, num_transitions, transitions

#-------------------------------------ALLOWS TO READ FILE-----------------------------
#print(file_read('automate.txt')[5])
def is_automaton_standard(file_txt): #checking if the automata is is_automaton_standard
    state=True #bool value check
    if len(file_read(file_txt)[2])==1: #cheking if there is multiple initial states, if so will go to line 38 and print False, meaning not is_automaton_standard
        initial_state=file_read(file_txt)[2][0] #collecting the int value of the 3rd line, which is the initial state
        array=file_read(file_txt)[5]
        for i in range(len(file_read(file_txt)[5])): #loop to lopp through all the elements in the 2d array
    
            if initial_state==array[i][2]:#loop to check if there is a match between the 3rd element of the 2d array

                state=False #if there is a match between the last element of the 2d array and the initial state, not is_automaton_standard automata
    else:
        return False 
    return state

#-------------------------------------PRINTS TABLE AUTOMATA------------------------------------------

def print_automata_array(file_name):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    result = ''
    file = open(file_name, 'r')
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

def is_automaton_deterministic(file_name): #function to check if the automata is is_automaton_deterministic
    if len(file_read(file_name)[2])==1:

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
            return True #this automata is is_automaton_deterministic
        else:
            return False
    else:
        return False
 
#------------------------------DETERMINIZE--------------------------------------------------------

def determinize_automaton(file_name):
    input_automaton = read_automaton(file_name)

    # Check if the automaton is already deterministic
    if not is_automaton_deterministic(file_name):
        num_symbols, num_states, initial_states, final_states, num_transitions, transitions = input_automaton

        # Create the alphabet of the automaton
        alphabet = [chr(ord('a') + i) for i in range(num_symbols)]  #Create the alphabet of the automaton using the number of symbols.

        # Create a dictionary to store transitions
        transition_dict = {}
        for state_from, symbol, state_to in transitions:
            state_from, state_to = int(state_from), int(state_to)
            if (state_from, symbol) in transition_dict:
                transition_dict[(state_from, symbol)].add(state_to)
            else:
                transition_dict[(state_from, symbol)] = {state_to}

        # Create the initial state of the deterministic automaton
        initial_state = frozenset(initial_states)

        # List to store the transitions of the deterministic automaton
        dfa_transitions = []

        # Use a queue to browse the new states created during the determination
        visited, queue = set(), [initial_state]
        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.add(current)

                # Process each symbol of the alphabet
                for symbol in alphabet:
                    next_states = set()
                    for state in current:
                        if (state, symbol) in transition_dict:
                            next_states |= transition_dict[(state, symbol)]

                    # Add the transition if it exists
                    if next_states:
                        dfa_transitions.append((current, symbol, frozenset(next_states)))
                        queue.append(frozenset(next_states))

        # Create a correspondence between the sets of states and the new states of the deterministic automaton
        state_mapping = {state: i for i, state in enumerate(sorted(visited))}

        # Find the final states of the deterministic automaton
        dfa_final_states = [state_mapping[state] for state in visited if state & set(final_states)]

        # Convert transitions to strings
        dfa_transitions_str = [f"{state_mapping[state_from]} {symbol} {state_mapping[state_to]}" for state_from, symbol, state_to in dfa_transitions]

        # Write the deterministic automaton in a new file
        with open('deterministic_automaton.txt', 'w') as file:
            file.write(f"{num_symbols}\n")
            file.write(f"{len(visited)}\n")
            file.write(f"{state_mapping[initial_state]}\n")
            file.write(' '.join(map(str, dfa_final_states)) + '\n')
            file.write(f"{len(dfa_transitions)}\n")
            file.writelines('\n'.join(dfa_transitions_str))
    
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
#------------------------------COMPLETE AUTOMATA-------------------------------------------

def complete_automaton(file_name):
    if not is_automaton_deterministic('automate.txt'):
        print("The automaton is not deterministic so it's not completable")
    else :
        input_automaton = read_automaton(file_name)

        if not is_automaton_complete(file_name):
            num_symbols, num_states, initial_states, final_states, num_transitions, transitions = input_automaton
            new_transitions = list(transitions)

            # Add a new stink state
            sink_state = num_states
            num_states += 1

            for state in range(num_states - 1):
                for symbol in range(num_symbols):
                    symbol_char = chr(ord('a') + symbol)
                    # Check if a transition with the same state and the same symbol does not already exist in transitions
                    if not any(transition for transition in transitions if transition[0] == str(state) and transition[1] == symbol_char):
                        new_transitions.append((state, symbol_char, sink_state))

            # Add transitions to the well state for missing symbols
            for symbol in range(num_symbols):
                symbol_char = chr(ord('a') + symbol)
                if not any(transition for transition in transitions if transition[0] == sink_state and transition[1] == symbol_char):
                    new_transitions.append((sink_state, symbol_char, sink_state))

            num_transitions = len(new_transitions)

            # Write the new automaton to a file
            with open("complete_automaton.txt", "w") as file:
                file.write(f"{num_symbols}\n{num_states}\n")
                file.write(" ".join(str(s) for s in initial_states) + "\n")
                file.write(" ".join(str(s) for s in final_states) + "\n")
                file.write(f"{num_transitions}\n")
                for transition in new_transitions:
                    file.write(" ".join(str(t) for t in transition) + "\n")

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
        if i in nb_of_final_states:
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



def standardize_finite_automaton(file_name):
    # open the file and read its contents
    with open(file_name, 'r') as f:
        number_of_symbols = int(f.readline())
        number_of_states = int(f.readline())
        initial_states = list(map(int, f.readline().split()))
        final_states = list(map(int, f.readline().split()))
        nb_of_transitions = int(f.readline())
        transitions = [f.readline().split() for _ in range(nb_of_transitions)]

    # check if the automaton is already standardized
    if is_automaton_standard(file_name):
        return

    # create a dictionary to store transitions
    transition_dict = {}
    for transition in transitions:
        state_from = int(transition[0])
        state_to = int(transition[2])
        label = transition[1]
        if state_from not in transition_dict:
            transition_dict[state_from] = []
        transition_dict[state_from].append((state_to, label))

    # create a new state to become the unique initial state
    new_initial_state = number_of_states
    number_of_states += 1

    # create new transitions from the new initial state to the old initial states
    for initial_state in initial_states:
        if initial_state in transition_dict:
            for state_to, label in transition_dict[initial_state]:
                transitions.append([str(new_initial_state), label, str(state_to)])
        else:
            # if there are no transitions from an initial state, add a transition to a new dead state
            transitions.append([str(new_initial_state), '', str(number_of_states)])
            number_of_states += 1

    # add the new initial state to the list of initial states if any old initial state was final
    if any(state in final_states for state in initial_states):
        final_states.append(new_initial_state)

    # update the initial states to be only the new initial state
    initial_states = [new_initial_state]

    # write the standardized automaton to a new file
    with open('standard_automaton.txt', 'w') as f:
        f.write(f"{number_of_symbols}\n")
        f.write(f"{number_of_states}\n")
        f.write(f"{' '.join(map(str, initial_states))}\n")
        f.write(f"{' '.join(map(str, final_states))}\n")
        f.write(f"{len(transitions)}\n")
        for transition in transitions:
            f.write(' '.join(transition) + '\n')




#-----------------------------GRAPHICAL REPRESENTATION------------------------------------
