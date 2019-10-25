import numpy as np
from numpy.random import choice
import math
import random
import matplotlib.pyplot as plt

def genPop(size): #initial population
    population = list()
    i = 0
    while (i < size):
        population.append(np.random.randint(8, size=8))
        i+=1
    return population
    
def fitness(child): #fitness function
    score1 = check_up(child) + check_down(child) + check_left(child) + check_right(child)
    score2 = check_upleft(child) + check_upright(child) + check_downleft(child) + check_downright(child)
    return (math.floor(28 - ((score1 + score2)/2)))

def check_up(child): #(x, y+1) 
    counter = 0
    for index1, c in enumerate(child):
        x = index1
        y = c + 1
        while (y < 8):
            for index2, j in enumerate(child):
                if (x == index2 and y == j):
                    counter += 1
                
            y += 1
    return counter
        
def check_down(child): #(x, y-1)
    counter = 0
    for index1, c in enumerate(child):
        x = index1
        y = c - 1
        while (y >= 0):
            for index2, j in enumerate(child):
                if (x == index2 and y == j):
                    counter += 1
                
            y -= 1
    return counter

def check_left(child): #(x-1, y)
    counter = 0
    for index1, c in enumerate(child):
        x = index1 - 1
        y = c
        while (x >= 0):
            for index2, j in enumerate(child):
                if (x == index2 and y == j):
                    counter += 1
                
            x -= 1
    return counter

def check_right(child): #(x+1, y)
    counter = 0
    for index1, c in enumerate(child):
        x = index1 + 1
        y = c
        while (x < 8):
            for index2, j in enumerate(child):
                if (x == index2 and y == j):
                    counter += 1
                
            x += 1
    return counter

def check_upleft(child): #(x-1, y+1)
    counter = 0
    for index1, c in enumerate(child):
        x = index1 - 1
        y = c + 1
        while (y < 8 and x >= 0):
            for index2, j in enumerate(child):
                if (x == index2 and y == j):
                    counter += 1
                
            y += 1
            x -= 1
    return counter

def check_upright(child): #(x+1, y+1)
    counter = 0
    for index1, c in enumerate(child):
        x = index1 + 1
        y = c + 1
        while (y < 8 and x < 8):
            for index2, j in enumerate(child):
                if (x == index2 and y == j):
                    counter += 1
                
            y += 1
            x += 1
    return counter

def check_downleft(child): #(x-1, y-1)
    counter = 0
    for index1, c in enumerate(child):
        x = index1 - 1
        y = c - 1
        while (y >= 0 and x >= 0):
            for index2, j in enumerate(child):
                if (x == index2 and y == j):
                    counter += 1
                
            y -= 1
            x -= 1
    return counter
    
def check_downright(child): #(x+1, y-1)
    counter = 0
    for index1, c in enumerate(child):
        x = index1 + 1
        y = c - 1
        while (y >= 0 and x < 8):
            for index2, j in enumerate(child):
                if (x == index2 and y == j):
                    counter += 1
                
            y -= 1
            x += 1
    return counter

def crossOver(parent1, parent2):
    #child = np.concatenate(parent1, parent2, axis=None)
    child = np.array([0, 0, 0, 0, 0, 0, 0, 0])
    i = 0
    j = 7
    while (i < 4):
        child[i] = parent1[i]
        child[j] = parent2[j]
        i += 1
        j -= 1
    if (random.randint(1,100) <= 5): #Mutation
        index = random.randint(0,7)
        child[index] = random.randint(0,7)
    return child
  
def breedPop(population):
    fScores = list() #list of fitness scores
    for index, p in enumerate(population):
        fScores.append(fitness(p))    
    probs = list() #list of probibilites
    for index2, p in enumerate(population):
        probs.append((fScores[index2]/sum(fScores)))
    newPop = list()
    i = 0
    print("Average fscore for this population:")
    print(math.floor(sum(fScores)/len(population))) #average fScore
    while(i<len(population)):
        array = np.arange(len(population)) #array of numbers from 0 to population size
        index = choice(array, p=probs)
        parent1 = population[index]
        
        index = choice(array, p=probs)
        parent2 = population[index]
        
        while (np.array_equal(parent2, parent1)):
            index = choice(array, p=probs)
            parent2 = population[index]
        child = crossOver(parent1, parent2)
        newPop.append(child)
        i += 1
        
    return newPop, (math.floor(sum(fScores)/len(population))) #new population and its average fScore

def checkSolution(population):
    for p in population:
        if (fitness(p) == 28):
            return True, p
        
    return False, 0

def printSolution(solution):
    print ("Solution:")
    for index, s in enumerate(solution):
        print ("(",index,",",s,")")
    print ("Fitness Score of Solution:")
    print (fitness(solution))
        
def main ():
    size = 100 #Size of the poulation
    print ("Population Size:")
    print (size)
    average_fScores = list()
    population = genPop(size)
    boolValue, solution = checkSolution(population)
    if (boolValue == True): #solution found
        printSolution(solution)
        plt.plot(average_fScores)
        fig = plt.figure()
        plt.show()
        return
    n = 0
    while(n<1000): #number of iterations
        population, average = breedPop(population)
        average_fScores.append(average)
        boolValue, solution = checkSolution(population)
        if (boolValue == True): #solution found
            printSolution(solution)
            plt.plot(average_fScores)
            fig = plt.figure()
            plt.show()
            return
        n+=1
    print ("Solution not found")
    return

#runs program!!!
main()

#Test Fitness
#array = np.random.randint(8, size=8)
#array = np.array([7, 1, 3, 0, 6, 4, 2, 5]) #A solution
#print ("Set of Queens:")
#print (array)
#print ("Fitness Score:")
#print (fitness(array))
    
#Test Crossover
#array1 = np.random.randint(8, size=8)
#print ("Set of Queens 1:")
#print (array1)    
#array2 = np.random.randint(8, size=8)
#print ("Set of Queens 2:")
#print (array2)  
#print ("crossover of the two:")
#print (crossOver(array1, array2))

