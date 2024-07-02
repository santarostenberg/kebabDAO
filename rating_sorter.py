import re

# Define the file paths
data_file = 'data.txt'
rating_file = 'rating.txt'

# Read the file contents
with open(data_file, 'r') as file:
    content = file.read()

print("Original content of data.txt:")
print(content)

# Split the content into entries based on the pattern
entries = content.split('Restaurant Name:')

print("Entries found:")
for entry in entries:
    print(entry)

# Define a list to hold restaurant data
restaurants = []

# Define a pattern to extract data
pattern = re.compile(r'''
    \s*Restaurant\sName:\s*(?P<name>.+?)\s*  # Restaurant Name
    Location:\s*(?P<location>.+?)\s*         # Location
    Rating\sS:\s*(?P<ratingS>\d*\.?\d*)\s*   # Rating S
    Rating\sJ:\s*(?P<ratingJ>\d*\.?\d*)\s*   # Rating J
    Comments:\s*(?P<comments>.*)             # Comments
    ''', re.VERBOSE)

# Parse each entry
for entry in entries:
    if not entry.strip():
        continue

    match = pattern.search(entry)
    if match:
        name = match.group('name').strip()
        ratingS = match.group('ratingS').strip()
        ratingJ = match.group('ratingJ').strip()
        
        # Convert ratings to floats, handle missing ratings
        ratingS = float(ratingS) if ratingS else 0
        ratingJ = float(ratingJ) if ratingJ else 0
        divisor = 2 if ratingS and ratingJ else 1
        average_rating = (ratingS + ratingJ) / divisor

        # Append to the list
        restaurants.append((name, average_rating))

        # Debug print for each restaurant
        print(f"Parsed restaurant: {name}, Rating S: {ratingS}, Rating J: {ratingJ}, Average Rating: {average_rating}")
    else:
        print(f"No match found for entry: {entry}")

# Sort the restaurants by average rating in descending order
restaurants.sort(key=lambda x: x[1], reverse=True)

# Debug print
print("Sorted restaurants:")
for idx, (name, avg_rating) in enumerate(restaurants, start=1):
    print(f"#{idx} {name} {avg_rating:.2f}")

# Write the results to the rating.txt file
with open(rating_file, 'w') as file:
    for idx, (name, avg_rating) in enumerate(restaurants, start=1):
        file.write(f"#{idx} {name} {avg_rating:.2f}\n")

# Ensure the file write is complete
print("rating.txt has been updated.")
