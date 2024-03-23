# This python project creates a list of Frida Kahlo paintings, their dates and the spot in the exhibition tour.

def create_paintings_list():
    # List of paintings
    paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']
    # Corresponding dates of the paintings
    dates = [1939, 1933, 1946, 1940]
    # Returns a list containing painting names and their dates
    return list(zip(paintings, dates))  

def generate_audio_tour_numbers(start, end):
    # Generates a list of sequential numbers for audio tour identifiers
    return list(range(start, end))

def combine_data(audio_tour_numbers, paintings):
    # Combines the audio tour numbers with the paintings
    return list(zip(audio_tour_numbers, paintings))  # Returns a list containing audio tour numbers and painting information

# Usage
paintings = create_paintings_list()  # Creates a list of paintings with their corresponding dates
audio_tour_numbers = generate_audio_tour_numbers(1, len(paintings) + 1)  # Generates audio tour numbers for the paintings
master_list = combine_data(audio_tour_numbers, paintings)  # Combines audio tour numbers with paintings
# Prints the master list containing tuples of audio tour numbers and painting information
print(master_list)  







