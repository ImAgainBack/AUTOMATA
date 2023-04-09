from functions_1 import *

b=3

while b!=7:
  try:
    a=int(input("Which automata do you want to analyse from 1 to 44?\n\n"))
    if 1<=a<=44:
      try:
        b=int(input("\n0- See graph of that automata\n"
            "1- If its deterministic\n"
            "2- If its standart and deterministic\n"
            "3- Standardize an automata\n"
            "4- Determinize automata\n"
            "5- If automamata is complete\n"
            "6- Complete the automata\n"
            "7- Quit\n"))
        if ((0<=b<=7) & (1<=a<=44)):
          if b== 0:
            display_finite_automaton(f'Int2-5-{a}.txt')
          elif b==1:
            if is_deterministic(f'Int2-5-{a}.txt'):
              print("This automata IS deterministric.\n\n")
            else:
              print("This automata is NOT deterministic.\n\n")
          elif b==2:
            if (is_automaton_standard(f'Int2-5-{a}.txt')==True & is_deterministic(f'Int2-5-{a}.txt')==True):
              print('This automata IS standard and IS deterministic.\n\n')
            elif (is_automaton_standard(f'Int2-5-{a}.txt')==True & is_deterministic(f'Int2-5-{a}.txt')==False):
              print('This automata IS standard and is NOT deterministic.\n\n')
            elif (is_automaton_standard(f'Int2-5-{a}.txt')==False & is_deterministic(f'Int2-5-{a}.txt')==True):
              print('This automata is NOT standard but IS deterministic.\n\n')
            else:
              print("This automata is NOT standard and IS NOT deterministic.\n\n")
          elif b==3:
            if not is_automaton_standard(f'Int2-5-{a}.txt') :
              standardize_finite_automaton(f'Int2-5-{a}.txt')
              display_finite_automaton('standard_automaton.txt')
            else :
              print("The automata is already standard")
          elif b==4:
            if is_deterministic(f'Int2-5-{a}.txt') :
              print('The automata is already deterministic')
            else :
              determinize_automaton(f'Int2-5-{a}.txt')
              display_finite_automaton('deterministic_automaton.txt')
          elif b==6:
            if not is_deterministic(f'Int2-5-{a}.txt'):
              print("The automaton is not deterministic so it's not completable\n\n")
            else :
              complete_automaton(f'Int2-5-{a}.txt')
              display_finite_automaton('complete_automaton.txt')
          elif b==5:
            if is_automaton_complete(f'Int2-5-{a}.txt') :
              print("This automata IS complete\n\n")
            else :
              print("This automata IS NOT complete\n\n")
          elif b==7:
            break
        else:
          print('Enter a value between 0 and 5.\n\n')
      except ValueError:
        print('Please, enter an integer between 0 and 5.\n\n')
  except ValueError:
    print('Please, enter an integer between 1 and 44.\n\n')
print('Program ended.\n')