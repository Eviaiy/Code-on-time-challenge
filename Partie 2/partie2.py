def all_decreasing_subsequences_of_digits(num):
    str_num = str(num)
    n = len(str_num)
    if n == 0:
        return []
    
    subsequences = [[] for _ in range(n)]

    # Initialize the subsequences with the single digit at each position
    for i in range(n):
        subsequences[i] = [str_num[i]]

    # Compute all possible decreasing subsequences
    for i in range(1, n):
        for j in range(i):
            if str_num[i] < str_num[j]:
                if len(subsequences[j]) + 1 > len(subsequences[i]):
                    subsequences[i] = subsequences[j] + [str_num[i]]

    # Flatten the list and convert sublists to strings, find the longest subsequence
    longest_sub = max([''.join(sub) for sub in subsequences], key=len, default='')
    return (longest_sub, num)

def process_file_and_save_grouped_sequences(filename, output_filename):
    subsequences = []
    with open(filename, 'r') as file:
        for line in file:
            num = int(line.strip())
            sub, original = all_decreasing_subsequences_of_digits(num)
            subsequences.append((len(sub), original, sub))
    
    # Sort subsequences by their length in descending order and group them
    subsequences.sort(reverse=True, key=lambda x: x[0])
    from itertools import groupby
    grouped_subsequences = groupby(subsequences, key=lambda x: x[0])

    # Save grouped sequences sorted by the longest subsequence length to the file
    with open(output_filename, 'w') as outfile:
        for length_group, group in grouped_subsequences:
            group_list = list(group)
            group_list.sort(reverse=True, key=lambda x: int(x[1]))
            seen = set()  # Set to track seen numbers and avoid duplicates
            outfile.write(f"Length {length_group}:\n")
            for length, original_number, subsequence in group_list:
                if original_number not in seen:
                    outfile.write(f"{original_number}\n")
                    seen.add(original_number)
            outfile.write("\n")

# Driver Code
if __name__ == "__main__":
    input_filename = 'Partie2/data2.txt'
    output_filename = 'all_grouped_longest_sequences.txt'
    process_file_and_save_grouped_sequences(input_filename, output_filename)
    print(f"Data processed and results have been grouped and saved to {output_filename}.")
 