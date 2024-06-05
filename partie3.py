def process_data(file_path):
    events = []
    
    # Read data from file
    with open(file_path, 'r') as file:
        for line in file:
            athlete_id, entry_time, exit_time = map(int, line.strip().split(','))
            events.append((entry_time, 'enter'))
            events.append((exit_time, 'exit'))
    
    # Sort events, with exits before entries at the same timestamp
    events.sort(key=lambda x: (x[0], x[1] == 'enter'))
    
    # Calculate the maximum number of athletes in the locker room at any time
    max_athletes = 0
    current_athletes = 0
    
    for event in events:
        if event[1] == 'enter':
            current_athletes += 1
        else:
            current_athletes -= 1
        max_athletes = max(max_athletes, current_athletes)
    
    return max_athletes

# Path to your data file
file_path = 'Partie3/data3.txt'
# Process the data and print the maximum number of athletes
max_athletes = process_data(file_path)
print(f"Maximum number of athletes in the locker room at any one time: {max_athletes}")
