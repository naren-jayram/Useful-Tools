'''
Objective: To demonstrate/simulate Birthday Paradox
Formulae: 
num_of_pairs = (no_of_item*(no_of_item-1))/2
chance_of_a_unique_pair = no_of_total_item-1/no_of_total_item
Chance_of_total_unique_pairs = (chance_of_a_unique_pair)^ num_of_pairs
Chance_of_some_match = (1 - Chance_of_total_unique_pairs)
'''
#!/usr/bin/python
import random
import math

while True:
    no_of_total_item = input("Enter the number of days in a year: ") 
    no_of_item = input("Enter the number of total students in a class room: ")
    print ("\n")
    num_of_pairs = (no_of_item*(no_of_item-1))/2
    num_of_pairs = float(num_of_pairs)
    chance_of_a_unique_pair = (float(no_of_total_item-1)/float(no_of_total_item))
    Chance_of_total_unique_pairs = math.pow(chance_of_a_unique_pair,num_of_pairs) 
    Chance_of_some_match = (1 - Chance_of_total_unique_pairs)
    
    # Converting to percentage
    chance_of_a_unique_pair = chance_of_a_unique_pair*100
    Chance_of_total_unique_pairs = Chance_of_total_unique_pairs*100
    Chance_of_some_match  = Chance_of_some_match *100
    
    print ("Chance of a unique birthday: %f percentage " %chance_of_a_unique_pair)
    print ("Chance of unique birthday in %d combinations: %f percentage" % (num_of_pairs,Chance_of_total_unique_pairs))
    print ("Chance of a match: %f percentage" %Chance_of_some_match)
    
    rand = []
    for x in range(no_of_item):
      rand.append(random.randint(1,no_of_total_item))
    
    print("Randomly selected Student Birtdays: ")
    print rand

    seen = set()
    uniq = []
    dup = []
    for item in rand:
        if item not in seen:
            uniq.append(item)
            seen.add(item)
        else:
            dup.append(item)
            seen.add(item)

    if dup:
        no_of_duplicates = len(dup)
        print("%d pair have the same birthday:" %no_of_duplicates)
        print dup
    else:
        print("Oops! No one is sharing the same birthday \n\n\n") 


    print("Do you wish try again...\n")
    loop_condition = str(raw_input("Press 'y' for Yes and 'n' for No: ")).lower().strip()
    if ((loop_condition ==  "n") or (loop_condition == "N")):
        exit(0)
    if ((loop_condition ==  "y") or (loop_condition == "Y")):
        continue
