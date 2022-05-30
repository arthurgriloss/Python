import pandas as pd
from math import sqrt
import random
import numpy as np
import matplotlib.pyplot as plt

###### VARIABLES ######
n_facilities = 10
s_production = 635
s_initial_storage = 1583
r_consumption = [87, 14, 86, 75, 42, 69, 79, 43, 77, 63]
r_initial_storage = [87, 14, 172, 75, 84, 69, 158, 86, 77, 63]
r_max_storage = [174, 28, 258, 150, 126, 138, 237, 129, 154, 189]
s_inv_cost = 0.03
r_inv_cost = [0.02, 0.03, 0.03, 0.02, 0.02, 0.03, 0.04, 0.04, 0.02, 0.04]
s_position = (440, 240)
r_position = [(160, 190), (230, 145), (135, 160), (460, 280), (290, 450), (80, 325), (0, 235), (50, 410), (305, 110), (305, 260) ]
T = 3

# Set same seed for replicable results
random.seed(4)
np.random.seed(4)

table_title = []
for _ in range(T):
    table_title.append(f"transp_cost_T{_+1}")   
    table_title.append(f"inv_cost_T{_+1}")   
    table_title.append(f"total_cost_T{_+1}")   
table_title.append("total_cost_all_periods")
table = np.array(table_title)

class Solution():
    def __init__(self, periods, n_facilities, off_n=10):
        """"Generate a offspring based on the problem.
            The way the genes of the offspring are generate depend
            on the number of periods and number of facilities that the
            retailer supplies.
            The genes the first row represents the sequence which
            the resources will be delivered (sequence chromosomes). 
            The genes of the second row are related to the number of 
            resources to deliver to the facilities (quantity chromosomes)"""

        self.periods = periods 
        self.n_facilities = n_facilities
        self.off_n = off_n
        self.offspring_list = []    # List with the genes of the offspring

        # Generate the offspring
        for _ in range(self.off_n):
            T_list = [] # List with the genes of the individual
            for _ in range(self.periods):
                s = np.array(range(self.n_facilities))  # Generates a list with len=n_facilities
                np.random.shuffle(s) # Shuffle the sequence of the list creating a random sequence of deliver for each individual
                T_list.append(np.array([s, np.random.randint(3, size=self.n_facilities)]).T)
            self.offspring_list.append(np.array(T_list))


    def crossover(self, fitness_list):
        for _ in range(self.periods):
            sequence_parent1 = self.offspring_list[fitness_list[0]][_][:, 0]
            quantity_parent1 = self.offspring_list[fitness_list[0]][_][:, 1]
            sequence_parent2 = self.offspring_list[fitness_list[1]][_][:, 0]
            quantity_parent2 = self.offspring_list[fitness_list[1]][_][:, 1]
            
            # Substitute 2 less fit individuals by the two new breeding
            # The first breeding has the sequence chromosome from parent1 and quantity chormosome from parent2
            # The second breeding has the sequence chormosome from parent2 and the quantity chormosome from parent1

            self.offspring_list[fitness_list[-1]][_][:, 0] = sequence_parent1
            self.offspring_list[fitness_list[-1]][_][:, 1] = quantity_parent2
            self.offspring_list[fitness_list[-2]][_][:, 0] = sequence_parent2
            self.offspring_list[fitness_list[-2]][_][:, 1] = quantity_parent1

    
    def mutation(self, fitness_list):
        for _ in range(self.periods):
            for position in fitness_list[2:8]:
                mutation_type = random.randint(0, 3)
                mutation_degree = random.randint(0, 3) # Bring mutation to all individuals (including breeding), but parents
                if mutation_type == 0:
                    np.random.shuffle(self.offspring_list[position][_][:mutation_degree, 0])
                elif mutation_type == 1:
                    np.random.shuffle(self.offspring_list[position][_][mutation_degree:, 0])
                elif mutation_type == 2:
                    np.random.shuffle(self.offspring_list[position][_][:mutation_degree, 1])
                elif mutation_type == 3:
                    np.random.shuffle(self.offspring_list[position][_][mutation_degree:, 1])

        


def eucl_distance(point1, point2):
    """Calculate the newtonian distance between 2 points"""
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

##### MAIN CODE #####

# INITIATION VARIABLES
best_cost = 10000000
old_error = 100000000
lower_cost =[]
avg_cost = []

s = Solution(T, n_facilities)   # Generate an offspring

epochs = 10000
for epoch in range(epochs):
    table = np.array(table_title)
    i=0 # COUNTER
    for indv in s.offspring_list:
        costs = []
        
        
        updated_storage = np.array(r_initial_storage[:n_facilities])    # Setting initial retailer storage
        upd_spp_storage = s_initial_storage # Setting initial supplier storage 

        for period in range(T):
            # INITIATION VARIABLES
            transp_cost_period = 0
            inv_cost_period = 0
            j = 0

            upd_spp_storage += s_production # Add produced supplies to the storage

            old_position = s_position   # Starting from the supplier location

            for element in indv[period]:
                faciltiy_to_deliv = r_position[element[0]]  # Select the location of the facility based on the position on the r_position list
                amount_to_deliv = element[1]    # Indicates the factor that should be used at delivering
                
                
                # Calculate storage before deliver 
                if updated_storage[element[0]] <= 0:
                    # Mutate the gene delivering amount to 1 or 2 in case the retailer has nothing stored
                    new_random_supply = random.randint(1, 2)    
                    s.offspring_list[i][period][j, 1] = new_random_supply
                    amount_to_deliv = new_random_supply
                elif updated_storage[element[0]] + r_consumption[element[0]] * amount_to_deliv >= r_max_storage[element[0]]:
                    # Mutate the gene delivering amount to 0 in case the retailer is at its max supply
                    s.offspring_list[i][period][j, 1] = 0
                    amount_to_deliv = 0
                else:
                    pass

                new_storage_value = r_consumption[element[0]] * amount_to_deliv + updated_storage[element[0]] # add delivered goods to the retailer storage
                upd_spp_storage -= r_consumption[element[0]] * element[1]   # subtract delivered goods given to the retailer storage
                updated_storage[element[0]] = new_storage_value # Update retailer storage

                
                j+=1

                # Deliver to storages that has resources to receive
                if amount_to_deliv != 0:
                    dist = eucl_distance(old_position, faciltiy_to_deliv)   # Calculate distance
                    transp_cost_period += dist    # Add cost distance

                    old_position = faciltiy_to_deliv    # Update vehicle position

                # Calculate storage after deliver 
                # new_storage_value = r_consumption[element[0]] * element[1] + updated_storage[element[0]]    # add delivered goods to the retailer storage
                # upd_spp_storage -= r_consumption[element[0]] * element[1]   # subtract delivered goods given to the retailer storage

                # updated_storage[element[0]] = new_storage_value 
                
                # if (new_storage_value > r_max_storage[element[0]]):
                #     inv_cost_period += new_storage_value * r_inv_cost[element[0]] * 200   # High penalty to surpass the max capacity
                # elif new_storage_value < 0 :
                #     inv_cost_period += -new_storage_value * r_inv_cost[element[0]] * 200 # High penalty since storage is bellow 0
                # else:
                #     inv_cost_period += new_storage_value * r_inv_cost[element[0]]   # calculate the inventary cost according to the uptodate inventary  
            
            
            updated_storage = updated_storage - np.array(r_consumption) # Consume after receive new supplies


            # Calculate supplier storage costs
            if upd_spp_storage < 0:
                # Warns and punish in case the solution brings a negative supplier capacy
                inv_cost_period += -upd_spp_storage * s_inv_cost * 200
                print(upd_spp_storage)
            else:
                inv_cost_period += upd_spp_storage * s_inv_cost # Add supplier inventary costs to the total inventary cost of the period
        
            # Save the costs
            costs.append(transp_cost_period)
            costs.append(inv_cost_period)
            costs.append(transp_cost_period + inv_cost_period)

        if T == 1:
            costs.append(costs[2]) # Appending total costs from all periods    
        elif T == 2:
            costs.append(costs[2] + costs[5]) # Appending total costs from all periods  
        else:  
            costs.append(costs[2] + costs[5] + costs[8]) # Appending total costs from all periods    
        table = np.vstack([table, np.array(costs)])
        
        i+= 1
    # Sort the index by the fittest to the less fit
    sorted_index_pos = [index for index, num in sorted(enumerate(table[1:, -1]), key=lambda x: x[-1])] 
    
    
    if epoch % 100 == 0:
        # Save intermadiary information to analyse progress
        lower_cost.append(float(table[sorted_index_pos[0]+1][-1]))
        avg_cost.append(np.mean((table[1:, -1]).astype(np.float64)))

    
    if epoch != epochs-1:
        # mutate and breed the population
        s.mutation(sorted_index_pos)
        s.crossover(sorted_index_pos)
    else:
        print("End of the simulation")


#### PLOT AND DATA SAVING ########
print("")
print("Fittest individual data:")
print("Cost table")
df = pd.DataFrame(np.array([table[sorted_index_pos[0] + 1]]))
df.columns = table[0]
print(df)
df.to_csv("cost_table_fittest.csv")

column = ["R0", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "S"]
fittest_idx = sorted_index_pos[0]
r_initial_storage.append(s_initial_storage)
r_consumption.append(0)
storage_list = [r_initial_storage]
storage = np.array(r_initial_storage)
upd_s_s = s_initial_storage
for _ in range(T):
    upd_s_s += s_production
    for i in range(10):
        cons_idx = s.offspring_list[fittest_idx][_][:, 0].tolist().index(i)
        delivered = np.array(r_consumption[i]) * s.offspring_list[fittest_idx][_][cons_idx, 1]
        storage[i] = storage[i] + delivered
        upd_s_s -= delivered

    print(storage)
    storage = storage - np.array(r_consumption)
    print(storage)
    

    storage[i+1] =  upd_s_s
    storage_list.append(storage)
    
    print("")
    print(f"Delivering sequence T{_+1}")
    print(s.offspring_list[fittest_idx][_][:, 0])
    print(s.offspring_list[fittest_idx][_][:, 1])


df = pd.DataFrame(storage_list)
df.columns = column
print("Storage Over the periods")
print(df)
df.to_csv("storage_over_periods.csv")





plt.plot(range(len(lower_cost)), lower_cost)
plt.plot(range(len(avg_cost)), avg_cost)
plt.legend(["Fittest cost", "Average Cost"])
plt.xlabel("100 epochs")
plt.ylabel("Total Cost")
plt.show()


i=0
j =0
fig, axs = plt.subplots(2, 2)
fig.tight_layout(pad=3.0)
for period in range(T):
    old_position = s_position
    if i == 2:
        i = 0
        j = 1
    for _ in s.offspring_list[sorted_index_pos[0]][period]:
        if _[1] != 0:
            destiny = r_position[_[0]]
            axs[i, j].plot([old_position[0], destiny[0]], [old_position[1], destiny[1]], color="grey")
            axs[1, 1].plot([old_position[0], destiny[0]], [old_position[1], destiny[1]], color="grey")
            old_position = destiny
        axs[i, j].plot([old_position[0], s_position[0]], [old_position[1], s_position[1]], color="grey")
        axs[1, 1].plot([old_position[0], s_position[0]], [old_position[1], s_position[1]], color="grey")
    axs[i, j].scatter(s_position[0], s_position[1], color="blue", alpha = 0.5)
    axs[1, 1].scatter(s_position[0], s_position[1], color="blue", alpha = 0.5)

    for pos in range(n_facilities):
        axs[i, j].scatter(r_position[pos][0], r_position[pos][1], color="blue", alpha = 0.5)
        axs[1, 1].scatter(r_position[pos][0], r_position[pos][1], color="blue", alpha = 0.5)
    axs[i, j].set_xlim((-10, 500))
    axs[i, j].set_ylim((0, 500))
    axs[1, 1].set_xlim((-10, 500))
    axs[1, 1].set_ylim((0, 500))
    axs[0, 0].set_title("a)")
    axs[1, 0].set_title("b)")
    axs[0, 1].set_title("c)")
    axs[1, 1].set_title("d)")
    i+=1
plt.show()


