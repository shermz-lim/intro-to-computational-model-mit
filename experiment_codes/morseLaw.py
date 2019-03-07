# simulates the doubling of technological prowess every year from 1980s to 2000s
# I just want to test the difference between using a linear and logarithmic scale

import pylab

x_values = list(range(1980, 2020))
y_values = []
current_y = 100 #arbitrary number of 100 

for _ in range(len(x_values)):
    y_values.append(current_y)
    # y doubles every year 
    current_y = current_y*2

# creates figure - linear
pylab.figure(1)
pylab.title('Representation of Morse\'s Law - linear scale')
pylab.xlabel('Year')
pylab.ylabel('Technology Index')
pylab.plot(x_values, y_values, 'b-')
pylab.savefig('morse_law_linear')

# creates figure - logarithmic
pylab.figure(2)
pylab.title('Representation of Morse\'s Law - log scale')
pylab.xlabel('Year')
pylab.ylabel('Technology Index')
pylab.semilogy() # change y axis to log scale
pylab.plot(x_values, y_values, 'b-')
pylab.savefig('morse_law_log')