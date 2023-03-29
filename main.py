from functions_1 import *

b=3

while b!=4:
  try:
    a=int(input("Which automata do you want to analyse from 1 to 44?\n"))
    if 1<=a<=44:
      try:
        b=int(input("0- See graph of that automata\n"
            "1- If its deterministic\n"
            "2- If its standart and deterministic\n"
            "3- Standardize an automata\n"
            "4- Quit\n"))
        if ((0<=b<=4) & (1<=a<=44)):
          if b== 0:
            display_finite_automaton('int-2-4-{a}.txt')
          elif b==1:
            print(is_automaton_deterministic(f'int2-4-{a}.txt'))
          elif b==2:
            if (is_automaton_standard(f'int2-4-{a}.txt')==True & is_automaton_deterministic(f'int2-4-{a}.txt')==True):
              print('This automata is standard and deterministic')
            elif (is_automaton_standard(f'int2-4-{a}.txt')==True & is_automaton_deterministic(f'int2-4-{a}.txt')==False):
              print('This automata is standard and is NOT deterministic')
            elif (is_automaton_standard(f'int2-4-{a}.txt')==False & is_automaton_deterministic(f'int2-4-{a}.txt')==True):
              print('This automata is NOT standard but is deterministic')
            else:
              print("This automata is NOT standard and isn't deterministic")
          elif b==3:
            standardize_finite_automaton(f'int2-4-{a}.txt')

        else:
          break
      except ValueError:
        print('Please, enter an integer between 0 and 4')
  except ValueError:
    print('Please, enter an integer between 1 and 44')
print('Program ended.')
