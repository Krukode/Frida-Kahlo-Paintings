# This python project creates a list of Frida Kahlo paintings, their dates and the spot in the exhibition tour.

# Create a list of paintings
paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']

# Create a list of dates
dates = [1939, 1933, 1946, 1940]

# Zip together the lists above
paintings = list(zip(paintings, dates))

# Add new paintings to the list
paintings.append(('The Broken Column', 1944))
paintings.append(('The Wounded Deer', 1946))
paintings.append(('The Wounded Deer', 1937))

print(paintings)

# Find the lenght of the paintings list
len(paintings)

# Generate and print  a list of identification numbers
audio_tour_number = list(range(1, 8))

print(audio_tour_number)

# Create and print a list that combines the paintings, dates and id number
master_list = list(zip(audio_tour_number, paintings))

print(master_list)







