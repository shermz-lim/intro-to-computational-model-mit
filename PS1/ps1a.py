###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # stores file as file object
    fileObj = open(filename)
    # initialize empty dict 
    name_weight_dict = {}

    # read each line of fileObj
    for line in fileObj.readlines():
        # splits line into a list of name, weight 
        name_weight = line.strip('\n').split(',')
        # stores name and weight in dictionary 
        name_weight_dict[name_weight[0]] = int(name_weight[1])

    return name_weight_dict


# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    
    # keep track of current trip 
    current_trip = []
    # keep track of current space available
    current_space_remaining = limit 

    # keep track of total trips 
    total_trips = []
    # keep track of name of all cows that are already fitted 
    total_cows = []

    # while not all cows are transported
    while len(total_cows) < len(cows):
        # keeps track of current cow that should be fitted
        cow_size = 0 
        cow_name = ''

        for name, weight in cows.items():
            # if the cow weight is greater than the current max size and still lesser than the 
            # remaining space, and the cow has not been fitted in a trip, 
            # the current cow to be fitted will be of cow name 
            if (weight > cow_size and weight <= current_space_remaining):
                if (name in total_cows):
                    continue 
                else:    
                    cow_size = weight 
                    cow_name = name 

        # if there is a cow that can be fitted 
        if cow_name:
            current_space_remaining -= cow_size
            current_trip.append(cow_name)
            total_cows.append(cow_name)

        else:
            # add current trip to total trips and reset current trip and space remaining
            total_trips.append(current_trip)
            current_trip = []
            current_space_remaining = limit 

    # appends last trip  
    total_trips.append(current_trip)
    # when all cows all assigned on a trip with the greedy algorithm, 
    return total_trips    


# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # brute force implementation 

    # set empty list of possible set of trips  
    possible_set_of_trips = []

    # generates set of all possible list of partitions with cow names 
    for partition in get_partitions(cows.keys()):
        
        # keeps track of whether any trip in this list exceeds weight limit 
        weight_exceed = False 

        # loops through the trip in this list 
        for trip in partition:
            
            value = 0 
            for cow in trip:
                value += cows[cow]

            # if weight of trip exceed limit  
            if value > limit:
                # set weight exceed to true and break 
                weight_exceed = True 
                break 

        # if none of the trips exceed weight limit, partition is a valid set of trips
        if not weight_exceed:
            # appends partition to possible set of valid trips 
            possible_set_of_trips.append(partition)

    # finds the shortest trip in the set of possible trips using linear search 
    min_trip_len = len(possible_set_of_trips[0])
    min_trip = possible_set_of_trips[0]

    for set_of_trip in possible_set_of_trips:
        if len(set_of_trip) < min_trip_len:
            min_trip_len = len(set_of_trip)
            min_trip = set_of_trip

    # return list of lists containing the minimal number of trips 
    return min_trip                     



        
# testing  


print(brute_force_cow_transport(load_cows('ps1_cow_data.txt')))

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass
