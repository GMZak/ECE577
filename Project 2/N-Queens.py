import random
import matplotlib.pyplot as plt
import time
#Generate inital population of chromosomes
def randomChromosome(NumberOfRows,NumberOfQueens):
    chromosome_list = []
    for i in range(NumberOfRows):
        gene = []
        for j in range(NumberOfQueens):
            gene.append(random.randint(1,n))
        gene.append(0)
        chromosome_list.append(gene)
    return chromosome_list


# Evaluate fitness check if they hit eachother
def fitness(population_list):
    i = 0
    hit = 0
    while i < len(population_list):
        j = 0
        hit = 0
        while j < n:
            k = j + 1

            while k < n:
                if population_list[i][j] == population_list[i][k]:
                    hit += 1
                if abs(j - k) == abs(population_list[i][j] - population_list[i][k]):
                    hit += 1
                k += 1
            j += 1
        population_list[i][len(population_list[j]) - 1] = hit
        i += 1

    for i in range(len(population_list)):
        min = i
        for j in range(i, len(population_list)):
            if population_list[j][n] < population_list[min][n]:
                min = j
        l = population_list[i]
        population_list[i] = population_list[min]
        population_list[min] = l
    return population_list

def cross_over(chromosome_list):
    for i in range(0,len(chromosome_list),2):
        k = 0
        offspring1 = []
        offspring2 = []
        while k<n:
            if(k<n//2):
                offspring1.append(chromosome_list[i][k])
                offspring2.append(chromosome_list[i+1][k])
            else:
                offspring1.append(chromosome_list[i+1][k])
                offspring2.append(chromosome_list[i][k])
            k+=1
        offspring1.append(0)
        offspring2.append(0)
        chromosome_list.append(offspring1)
        chromosome_list.append(offspring2)
    return chromosome_list

def mutation(chromosome_list):
    mutation_list=[]
    i = 0
    while i<p//2:
        new_mut = random.randint(p//2,p-1)
        if new_mut not in mutation_list:
            mutation_list.append(new_mut)
            chromosome_list[new_mut][random.randint(0,n-1)]=random.randint(1,n-1)
            i+=1
    return chromosome_list

def showRes(res):
    l = len(res)
    plt.figure(figsize=(6, 6))
    plt.scatter([x+1 for x in range(l - 1)], res[:l - 1])
    for i in range(l):
        plt.plot([0.5, l - 0.5], [i + 0.5, i + 0.5], color = "k")
        plt.plot([i + 0.5, i + 0.5], [0.5, l - 0.5], color = "k")
timer_list = []
for i in range(10,55,5):
    n=i #num of queens
    p=1000 #population size
    current_generation = [] #Current Generation
    new_generation = [] #New Generation
    print('------------ Current Number of Queens : {0} ----------------'.format(i))
    current_generation = randomChromosome(p,n)
    current_generation = fitness(current_generation)
    generation_count = 1
    while True:
        print(" ")
        print("Generation ",generation_count)
        tic = time.time()
        current_generation = current_generation[0:p//2]
        next_generation = cross_over(current_generation)
        next_generation = mutation(next_generation)
        current_generation = next_generation
        current_generation = fitness(current_generation)
        toc = time.time()
        if current_generation[0][n] == 0:
            print("Solution Found: ", current_generation[0])
            # showRes(current_generation[0])
            timer_list.append(toc - tic)
            break
        else:
            pass
            #print("Best Solution: ", current_generation[0])
        generation_count+=1

print(timer_list)
plt.figure(figsize=(6, 6))
plt.plot(timer_list,range(10,55,5))
plt.xlabel("Time")
plt.ylabel("Number of queens")
plt.show()