import sys
import math


def getmodulefuel(mass,totalfuel):

    #takes an integer mass_value and calculated the total mass value
    #
    #example:
    #At first, a module of mass 1969 requires 654 fuel. Then, this fuel
    #requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel,
    #which requires 21 fuel, which requires 5 fuel, which requires
    #no further fuel. So, the total fuel required for a module of mass
    #1969 is 654 + 216 + 70 + 21 + 5 = 966.

    #calculate the fuel required for the given mass.
    mass = math.trunc(mass/3) - 2

    if mass <= 0:
        #if the resultant math is less than zero, we're done!
        return totalfuel
    else:
        #if the resultant mass is more than zero, add the total totalfuel
        #and keep going
        totalfuel = totalfuel + mass
        return getmodulefuel(mass,totalfuel)


if __name__ =="__main__":

    #read the numbers in
    readfile = open('aoc_day1_1.txt')

    module_masses = []
    totalfuel = 0

    #go through each number and calculate the fuel
    for line in readfile:
        module_masses.append(int(line))
        totalfuel = totalfuel + getmodulefuel(int(line),0)
        #print(line)

    #print the total fuel to the terminal
    print(totalfuel)
