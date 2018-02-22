#This program creates a randomized list of 2 dimentional polynomial equations
#It then tests those equations against a know answer and decreases the chance
#that incorrect equations will be processed and increases the chances that
#correct equations will be processed 

import random
#This Function creates random input
def rand_input():
    return random.uniform(1, 10)
#This fuction creates and answer fuction for the program to learn
def eq_answer (x):
    out = 3 * x + 1
    return out

#This function creates random weights between a range of low and high
def random_weight(low, high):
    number = random.uniform(low, high)
    return number

#This function tests to see if equation should be calculated
def roll(x):
    number = random.uniform(0,1)
    if x > number:
        return True
    else:
        return False

#This function outputs new fuctions based on the current best function
def new_equation(top_equation): 
    #new random weight distribution is current best weight +- 0.1
    replacement_equation = (random_weight(top_equation[0] - new_equation_weight_range_lower, top_equation[0] + new_equation_weight_range_upper) ,random_weight(top_equation[1] - new_equation_weight_range_lower, top_equation[1] + new_equation_weight_range_upper) , random_weight(top_equation[2] - new_equation_weight_range_lower, top_equation[2] + new_equation_weight_range_upper) , initial_equation_chance )
    
    return replacement_equation




#Lists of randomized equations
equation_list = []
top_chance = 0    
number_equations = 1000
initial_equation_chance = 1.0
min_starting_weight_range = -2.0
max_starting_weight_range = 2.0
new_equation_weight_range_upper = 0.1
new_equation_weight_range_lower = 0.1
top_equation = (random_weight(min_starting_weight_range, max_starting_weight_range), random_weight(min_starting_weight_range, max_starting_weight_range) , random_weight(min_starting_weight_range, max_starting_weight_range), initial_equation_chance)

#Here we are creating a list of weights and fire chances to use for training
for i in range(number_equations): # of equations
    entry = (random_weight(min_starting_weight_range, max_starting_weight_range), random_weight(min_starting_weight_range, max_starting_weight_range) , random_weight(min_starting_weight_range, max_starting_weight_range), initial_equation_chance) #entry in list format (3-tuple)
    equation_list.append(entry)                 # = mutiplyier of x, + constant, chance to fire


#Training and testing part
train_counter = 0
while (train_counter < 1000): #100 training runs


#This part takes a random input and calculates through all the functions
    print ("run ", train_counter)
    input_val = rand_input()
    answer_list = [] #to hold calculations answers
    fire_chance_mod = 0
    counter = 0

    for i in equation_list: #goes through equation list and generates answer list
        chance = roll(i[3])
        #print(chance)
        #input()

        if chance == True:
            answer = (input_val * input_val * i[0]) + (input_val * i[1])  + i[2]
            appended_entry = (counter , answer) #answer output is tuples = (positions on equation list and answer)
            answer_list.append(appended_entry)
        counter += 1

#This is the learning part of the code
#This loop tests answers versus actual answers and then adjusts equations usage chance 
    for i in answer_list:
        fire_chance_mod = abs(i[1] - eq_answer(input_val)) #absolute value of difference
        fire_chance_mod = (fire_chance_mod / eq_answer(input_val)) #creates percentage difference 
        growth_factor = 0.15 #initailizes growth factor for answers that are near correct

        equa_holder = equation_list [i[0]] #access of current answerlist to corresponding position on equation list
        old_fire_chance = equa_holder[3] #access of usage percentage
        new_fire_chance = old_fire_chance - fire_chance_mod + growth_factor #calculates a new usage chance
        if new_fire_chance > top_chance:
            top_chance = new_fire_chance
            top_equation = equa_holder
        #print("New Fire Chance = ",new_fire_chance)
        if new_fire_chance < 0.00: #removes completely wrong equations
            equa_holder = new_equation(top_equation) #generates replacement equation close to best equation
            #print("equation holder = ",equa_holder)
            equation_entry = (equa_holder[0],equa_holder[1],equa_holder[2], initial_equation_chance) 
        else:
            equation_entry = (equa_holder[0],equa_holder[1],equa_holder[2],new_fire_chance) #updates entry list with new 3-tuple
        #print("equation entry = ", equation_entry) 
        #print(" OLD = ", equation_list[i[0]])
        equation_list[i[0]] = equation_entry
        #print(" NEW = ", equation_list[i[0]])
        #input()
        #for e in equation_list:
            #print(e)
        #input()
    
    train_counter += 1 #tracks training iterations
    





for i in equation_list:
    print(i)
print("Best Equation = ", top_equation)

    
    


    

        
        


    
