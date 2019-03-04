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
    
    # base case
    if target_weight in egg_weights:
        return 1

    smallest_num_eggs = float('inf')

    # recursive case: 1 branch for each diff. egg weights 
    for weight in egg_weights:
        remaining_weight = target_weight - weight 
        print(remaining_weight)

        # only enter branch if remaining weight can be fulfilled by egg weights 
        if remaining_weight > 0:
            
            try:
                # checks whether recursive solution is already in memo 
                recursive_num_eggs = memo[remaining_weight]
            except KeyError:
                recursive_num_eggs = dp_make_weight(egg_weights, remaining_weight, memo)  
                memo[target_weight] = (recursive_num_eggs + 1)

            if recursive_num_eggs < smallest_num_eggs:
                smallest_num_eggs = recursive_num_eggs    

    return (smallest_num_eggs + 1)





# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
