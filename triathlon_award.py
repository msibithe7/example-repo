# Define a function to determine the award
def determine_award(swim_time, bike_time, run_time):
    total_time = swim_time + bike_time + run_time

    if total_time <= 120:
        return "Gold Medal"
    elif total_time <= 150:
        return "Silver Medal"
    elif total_time <= 180:
        return "Bronze Medal"
    else:
        return "Participation Award"

# Get the swim, bike, and run times from the user
swim_time = float(input("Enter the swim time (minutes): "))
bike_time = float(input("Enter the bike time (minutes): "))
run_time = float(input("Enter the run time (minutes): "))

# Determine and print the award
award = determine_award(swim_time, bike_time, run_time)
print("Your award is:", award)



# Define a function to calculate the total time
def calculate_total_time(swim_time, bike_time, run_time):
    total_time = swim_time + bike_time + run_time
    return total_time

# Get the swim, bike, and run times from the user
swim_time = float(input("Enter the swimming time (minutes): "))
bike_time = float(input("Enter the cycling time (minutes): "))
run_time = float(input("Enter the running time (minutes): "))

# Calculate and print the total time
total_time = calculate_total_time(swim_time, bike_time, run_time)
print("The total time to complete the triathlon is:", total_time, "minutes")

# Determine and print the award
if total_time <= 120:
    print("Your award is: Gold Medal")
elif total_time <= 150:
    print("Your award is: Silver Medal")
elif total_time <= 180:
    print("Your award is: Bronze Medal")
else:
    print("Your award is: Participation Award")


    # Define a function to calculate the total time
def calculate_total_time(swim_time, bike_time, run_time):
    total_time = swim_time + bike_time + run_time
    return total_time

# Get the swim, bike, and run times from the user
swim_time = float(input("Enter the swimming time (minutes): "))
bike_time = float(input("Enter the cycling time (minutes): "))
run_time = float(input("Enter the running time (minutes): "))

# Calculate and print the total time
total_time = calculate_total_time(swim_time, bike_time, run_time)
print("The total time to complete the triathlon is:", total_time, "minutes")

# Determine and print the award
if total_time <= 100:
    print("Your award is: Provincial colours")
elif total_time <= 105:
    print("Your award is: Provincial half colours")
elif total_time <= 110:
    print("Your award is: Provincial scroll")
else:
    print("Sorry, you did not qualify for an award.")


    # Define a function to calculate the total time
def calculate_total_time(swim_time, bike_time, run_time):
    total_time = swim_time + bike_time + run_time
    return total_time

# Get the swim, bike, and run times from the user
swim_time = float(input("Enter the swimming time (minutes): "))
bike_time = float(input("Enter the cycling time (minutes): "))
run_time = float(input("Enter the running time (minutes): "))

# Calculate and print the total time
total_time = calculate_total_time(swim_time, bike_time, run_time)
print("The total time to complete the triathlon is:", total_time, "minutes")

# Determine and print the award
if total_time <= 100:
    award = "Provincial colours"
elif total_time <= 105:
    award = "Provincial half colours"
elif total_time <= 110:
    award = "Provincial scroll"
else:
    award = "No award"

print("Your award is:", award)
