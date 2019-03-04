###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================


# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # solution: recursion + memoization. Recursion problem to solve: minimum no. of eggs needed to fulfil target weight 

    # base case: only 1 egg needed when 1 of the egg can fulfil the target weight 
    if target_weight in egg_weights:
        return 1

    # initialize smallest number of eggs for this node as infinity 
    # if no branch can be entered, node will need infinity no. of eggs 
    smallest_num_eggs = float('inf')

    # recursive case: enters 1 branch for each diff. egg weights 
    for weight in egg_weights:
        remaining_weight = target_weight - weight 

        if remaining_weight > 0:
            try:
                # checks whether recursive solution is already in memo 
                recursive_num_eggs = memo[remaining_weight]
            except KeyError:
                # node's possible no. of eggs = 1 + min no. of eggs in branch node 
                recursive_num_eggs = dp_make_weight(egg_weights, remaining_weight, memo) + 1
                # stores solution in memo for future use 
                memo[remaining_weight] = recursive_num_eggs

            if recursive_num_eggs < smallest_num_eggs:
                # keeps track of the smallest no. of eggs 
                smallest_num_eggs = recursive_num_eggs    

    # return min no. of eggs out of all possible ones 
    return smallest_num_eggs





# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 20)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))


# Problem B2: write-up

# 1. if there were 30 different egg weights, there will be an exponential increase 
# in the number of recursive calls which results in an exponential increase in 
# runtime 

# 2. The objective would be to pick the egg with greatest weight at each stage. 
# Greedy function: minimise no. of eggs. Constraints - weight limit cannot be exceeded.
# Pick the egg with highest weight as long as it is below the target weight. 

# 3. Yes. It will not return the optimal solution when 1 is not one of the 
# egg weights. Having an egg with weight of 1 ensures that the optimal solution is 
# always derived at by following the greedy algorithm. 