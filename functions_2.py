from functions_1 import *

def determinized():
    def find_duplicates(lst, indices):
        seen = set()
        duplicates = set()
        for i, sublist in enumerate(lst):
            key = tuple(sublist[i] for i in indices)
            if key in seen:
                duplicates.add(i)
            seen.add(key)
        return duplicates

    duplicates = find_duplicates(data_6th_line, [0,1])
        
    if duplicates==set():
        return True
    else:
        return False

def complete(list):
    if len(third_line())==1:
        
        return True
    else:
        return False
    
print(determinized())
