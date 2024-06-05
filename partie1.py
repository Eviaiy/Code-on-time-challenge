import pandas as pd

def main():
    try:
        # Read the data from the file
        data = pd.read_csv('Partie1/data1.txt', header=None, names=['BibNumber', 'Country', 'Time'])
    except FileNotFoundError:
        print("The file 'race_data.txt' was not found.")
        return
    except pd.errors.EmptyDataError:
        print("The file 'race_data.txt' is empty.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    # Sum the times for each country
    country_times = data.groupby('Country')['Time'].sum()

    if country_times.empty:
        print("No data was processed.")
    else:
        # Determine the country with the lowest total time
        winning_country = country_times.idxmin()
        winning_time = country_times.min()

        print(f"The winning country is {winning_country} with a total time of {winning_time} milliseconds.")

if __name__ == "__main__":
    main()
