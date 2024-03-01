# Create a list of sandwiches to make
# Then create an empty list of finished sandiwches
sandwiches = ['reuben', 'chicken pesto', 'barbecue', 'roast beef', 'club']
finished_sandiches = []

# Move sandwiches one by one to finished, printing a message for each one
while sandwiches:
    current_sandwich = sandwiches.pop()
    print(f"I made your {current_sandwich.title()} sandwich!")
    finished_sandiches.append(current_sandwich)

# print each sandwich that has been made
print("The following sandiwiches have been made:")

for finished_sandwich in finished_sandiches:
    print(finished_sandwich.title())