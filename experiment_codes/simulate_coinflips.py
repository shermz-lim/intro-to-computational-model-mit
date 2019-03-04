# simulation model - use principle of inferential statistics to infer 
# population value from a sample 
# depending upon the law of large numbers - This law states that in repeated independent
# experiments (e.g., flipping a fair coin 100 times and counting the fraction of
# heads) with the same expected value (0.5 in this case), the average value of the 
# experiments approaches the expected value as the number of experiments goes to infinity.

import random 

def flip(numFlips):
    heads = 0.0
    for _ in range(numFlips):
        if random.random() < 0.5:
            heads += 1
    return heads/numFlips
    
def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for _ in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    return mean

if __name__ == "__main__":
    print(flipSim(100, 100000))