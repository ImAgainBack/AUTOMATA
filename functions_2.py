from functions_1 import * #getting functions from functions_1

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

def complete(list): 
    if len(third_line())==1:
        
        return True
    else:
        return False
    
print(determinized())
