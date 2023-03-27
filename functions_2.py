from functions_1 import * #getting functions from functions_1
import graphviz
from itertools import groupby

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

    return True
    
print(determinized())
