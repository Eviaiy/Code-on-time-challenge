import random
import math

# Function to read data from a file
def read_data(file_path):
    athletes = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')  # Adjust separator if necessary
            bib_number = int(parts[0])
            time = float(parts[1])
            athletes[bib_number] = time
    return athletes

# Function to calculate total team time including relay transmission times
def calculate_team_time(team, athlete_times):
    total_time = 0
    for i in range(len(team)):
        total_time += athlete_times[team[i]]
        if i > 0:
            relay_time = (athlete_times[team[i]] - athlete_times[team[i-1]])**2
            total_time += relay_time
    return total_time

# Function to calculate the score
def calculate_score(teams, athlete_times):
    team_times = [calculate_team_time(team, athlete_times) for team in teams]
    return abs(max(team_times) - min(team_times))  # Want to minimize this value

# Function to swap two random elements in a list
def swap_random_elements(lst):
    idx1, idx2 = random.sample(range(len(lst)), 2)
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1]

# Simulated annealing algorithm to find the best team arrangement
def simulated_annealing(athletes, temp, cooling_rate, team_size, iterations, save_interval):
    bib_numbers = list(athletes.keys())
    random.shuffle(bib_numbers)
    best_state = bib_numbers[:]
    best_score = calculate_score([best_state[i:i + team_size] for i in range(0, len(bib_numbers), team_size)], athletes)
    
    current_temp = temp
    
    for iteration in range(iterations):
        new_state = best_state[:]
        swap_random_elements(new_state)
        new_score = calculate_score([new_state[i:i + team_size] for i in range(0, len(new_state), team_size)], athletes)
        
        if new_score < best_score:
            best_state = new_state[:]
            best_score = new_score
            print(f"New best score {best_score} at iteration {iteration}")
        
        elif math.exp((best_score - new_score) / current_temp) > random.random():
            best_state = new_state
        
        current_temp *= cooling_rate
        
        if iteration % save_interval == 0:
            print(f"Iteration {iteration}: Current Best Score {best_score}")
            with open('best_teams.txt', 'w') as file:
                file.write(f"Iteration {iteration}: Best Teams {' '.join(map(str, best_state))}, Score: {best_score}\n")

    return ' '.join(map(str, best_state))

# Running the algorithm
file_path = 'Partie4/data4e.txt'  # Specify the correct path to your data file
athletes = read_data(file_path)
temperature = 1.0
cooling_rate = 0.999
team_size = 128
iterations = 800000000
save_interval = 80000000

final_teams = simulated_annealing(athletes, temperature, cooling_rate, team_size, iterations, save_interval)
print("Final best arrangement:", final_teams)
